import json
import sys
from shapely import Polygon
from shapely.geometry import shape

from analysis import count_by_zone, intersecting_parcels, parcels_above_threshold, total_active_area
from spatial import Parcel

##########################################
# BEGIN
##########################################

##########################################
# LOAD parcel_data from JSON file
# CONVERT parcel_data into Parcel objects
# STORE in parcel_list
##########################################
with open('data/parcels.json', 'r') as file:
    parcels = json.load(file)

parcel_list = []
for parcel in parcels:
    parcel_id = parcel.pop("parcel_id")
    geometry = shape(parcel.pop("geometry"))
    attributes = parcel

    parcel = Parcel(parcel_id=101, geometry=geometry, attributes=attributes)
    parcel_list.append(parcel)

##########################################
# IF parcel_list is empty THEN
#     PRINT "No parcels found."
#     STOP
# END IF
##########################################
if len(parcel_list) == 0:
    print("No parcels found.")
    sys.exit()

##########################################
# GET THRESHOLD AND STORE TO threshold
# GET DEVELOPMENT AREA ZONE AND STORE TO development_area_zone
##########################################
threshold = 6500
development_area_zone = "Commercial"


##########################################
# SET total_active_area = 0
# SET parcel_exceed_list = []
# SET zone_parcel_dict = {}
# SET parcel_intersect_list = []

# FOR EACH parcel IN parcel_list
# IF parcel.active is TRUE
#     total_active_area = total_active_area + parcel.area
# END IF

# IF parcel.area > threshold
#     APPEND parcel to parcel_exceed_list
# END IF

# IF parcel.zone A KEY OF DICT zone_parcel_dict
#     SET zone_parcel_dict[parcel.zone] = zone_parcel_dict[parcel.zone] + 1
# ELSE
#     SET zone_parcel_dict[parcel.zone] = 1
# END IF

# IF parcel.zone IS EQUAL TO development_area_zone
#     APPEND parcel to parcel_intersect_list
# END IF
# END FOR
##########################################
active_area = total_active_area(parcel_list)
parcel_exceed_list = parcels_above_threshold(parcel_list, threshold)
zone_parcel_dict = count_by_zone(parcel_list)
parcel_intersect_list = intersecting_parcels(parcel_list, development_area_zone)


##########################################
# DISPLAY active_area AS TOTAL AREA OF ALL ACTIVE PARCEL
# DISPLAY parcel_exceed_list AS LIST OF PARCELS THAT EXCEED THE THRESHOLD
# DISPLAY zone_parcel_dict AS DICT KEY VALUE PAIR OF ZONE AND PARCEL COUNT OF THAT ZONE
# DISPLAY parcel_intersect_list AS LIST OF PARCELS WITH ZONE EQUAL TO DEVELOPMENT AREA ZONE
##########################################
print(f"Total Active Area is: {active_area}")
print(f"There are {len(parcel_exceed_list)} parcels that exceeded the threshold of {threshold}. The full list of parcels are in variable parcel_exceed_list.")
print(f"The parcel count per zone are in this dict: {zone_parcel_dict}")
print(f"There are {len(parcel_intersect_list)} parcels that have zone [{development_area_zone}]. The full list of parcels are in variable parcel_intersect_list.")


##########################################
# SAVE OUTPUT TO JSON FILE
##########################################
summary = {
    "parameters": {
        "threshold": threshold,
        "development_area_zone": development_area_zone
    },
    "result": {
        "active_area": active_area,
        "parcel_exceed_list": parcel_exceed_list,
        "zone_parcel_dict": zone_parcel_dict,
        "parcel_intersect_list": parcel_intersect_list
    }
}
with open('output/summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2)

##########################################
# END
##########################################
