import json
from shapely import Polygon
from shapely.geometry import shape

from analysis import count_by_zone, intersecting_parcels, parcels_above_threshold, total_active_area
from spatial import Parcel

# Using a context manager ('with') ensures the file closes automatically
with open('data/parcels.json', 'r') as file:
    parcels = json.load(file)


parcel_list = []
for parcel in parcels:
    parcel_id = parcel.pop("parcel_id")
    geometry = shape(parcel.pop("geometry"))
    attributes = parcel

    parcel = Parcel(parcel_id=101, geometry=geometry, attributes=attributes)
    parcel_list.append(parcel)
    # print(parcel_id)
    # print(geometry)
    # print(attributes)
    # print(parcel)
    # print(parcel.area())
    # print(parcel.attributes["area_sqm"])
    # break



geom = Polygon([
        (121, 14),
        (122, 14),
        (122, 15),
        (121, 15)
    ])

development_zone = "Residential"

threshold = 100000
active_area = total_active_area(parcel_list)
parcel_exceed_list = parcels_above_threshold(parcel_list, threshold)
zone_parcel_dict = count_by_zone(parcel_list)
parcel_intersect_list = intersecting_parcels(parcel_list, development_zone)

print(f"Active Area: {active_area}")
print(f"parcel_exceed_list Area: {len(parcel_exceed_list)}")
print(f"zone_parcel_dict", zone_parcel_dict)
print(f"parcel_intersect_list Area: {len(parcel_intersect_list)}")