import math
from typing import Union
from shapely.geometry import Polygon, MultiPolygon

from spatial import Parcel


# # from gemini
# def approximate_area_m2(geometry: Union[Polygon, MultiPolygon]) -> float:
#     """
#     Approximates the area of a WGS84 Polygon or MultiPolygon in square meters.
#     """
#     # Both Polygon and MultiPolygon have a centroid and an area attribute
#     lat: float = geometry.centroid.y

#     # 1 deg lat ~ 111.32km, 1 deg lon ~ 111.32km * cos(lat)
#     meters_per_degree_lat: float = 111320.0
#     meters_per_degree_lon: float = 111320.0 * math.cos(math.radians(lat))

#     # Scaling factor for area is (lat_scale * lon_scale)
#     area_meters: float = geometry.area * meters_per_degree_lat * meters_per_degree_lon

#     return area_meters


def total_active_area(parcels: list[Parcel]) -> float:
    total_area = 0
    for parcel in parcels:
        if parcel.attributes["is_active"] == True:
            total_area += parcel.area()
    return total_area


def parcels_above_threshold(parcels: list[Parcel], threshold: float) -> list:
    return [parcel for parcel in parcels if parcel.area() > threshold]


def count_by_zone(parcels: list[Parcel]) -> dict:
    zone_dict = {}
    for parcel in parcels:
        zone = parcel.attributes["zone"]
        if zone in zone_dict:
            zone_dict[zone] += 1
        else:
            zone_dict[zone] = 1
    return zone_dict

def intersecting_parcels(parcels: list[Parcel], zone) -> list:
    return [parcel for parcel in parcels if parcel.attributes["zone"] == zone]