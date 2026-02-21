import math

from shapely.geometry import Point as ShapelyPoint
from shapely.geometry.base import BaseGeometry

# from analysis import approximate_area_m2


class SpatialObject:
    def __init__(self, geometry: BaseGeometry):
        self.geometry = geometry

    def bbox(self):
        return self.geometry.bounds

    # check for polygon and multipolygon from gemini
    def area(self) -> float:
        # 1. Structural Validation: Ensure geometry isn't empty
        if self.geometry.is_empty:
            return 0.0

        # 2. Validity Check: Ensure geometry is topologically 'valid'
        # (e.g., no self-intersecting rings in a polygon)
        if not self.geometry.is_valid:
            raise ValueError("Cannot calculate area: Geometry is invalid (e.g., self-intersecting).")

        # 3. Type Validation: Only attempt math if it's a surface (Polygon/MultiPolygon)
        # Points and Lines have an area of 0.0 in Shapely.
        if self.geometry.area <= 0:
            return 0.0

         # Both Polygon and MultiPolygon have a centroid and an area attribute
        lat: float = self.geometry.centroid.y

        # 1 deg lat ~ 111.32km, 1 deg lon ~ 111.32km * cos(lat)
        meters_per_degree_lat: float = 111320.0
        meters_per_degree_lon: float = 111320.0 * math.cos(math.radians(lat))

        # Scaling factor for area is (lat_scale * lon_scale)
        area_meters: float = self.geometry.area * meters_per_degree_lat * meters_per_degree_lon

        return area_meters

    def intersects(self, other) -> bool:
        return self.geometry.intersects(other.geometry)


class Parcel(SpatialObject):
    """
    Parcel = spatial object + structured attributes.
    """
    def __init__(self, parcel_id, geometry, attributes: dict):
        super().__init__(geometry)
        self.parcel_id = parcel_id
        self.attributes = attributes

    def as_dict(self):
        return {
            "parcel_id": self.parcel_id,
            "bbox": self.bbox(),
            "attributes": self.attributes
        }