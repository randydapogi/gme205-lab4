import math
from typing import Union
from shapely.geometry import Polygon, MultiPolygon


# from gemini
def approximate_area_m2(geometry: Union[Polygon, MultiPolygon]) -> float:
    """
    Approximates the area of a WGS84 Polygon or MultiPolygon in square meters.
    """
    # Both Polygon and MultiPolygon have a centroid and an area attribute
    lat: float = geometry.centroid.y

    # 1 deg lat ~ 111.32km, 1 deg lon ~ 111.32km * cos(lat)
    meters_per_degree_lat: float = 111320.0
    meters_per_degree_lon: float = 111320.0 * math.cos(math.radians(lat))

    # Scaling factor for area is (lat_scale * lon_scale)
    area_meters: float = geometry.area * meters_per_degree_lat * meters_per_degree_lon

    return area_meters