from spatial import Parcel


##########################################
# FOR EACH parcel IN parcel_list
#     IF parcel.active is TRUE
#         active_area = active_area + parcel.area
#     END IF
# END FOR
##########################################
def total_active_area(parcels: list[Parcel]) -> float:
    total_area = 0
    for parcel in parcels:
        if parcel.attributes["is_active"] == True:
            total_area += parcel.area()
    return total_area


##########################################
# FOR EACH parcel IN parcel_list
#     IF parcel.area > threshold
#         APPEND parcel to parcel_exceed_list
#     END IF
# END FOR
##########################################
def parcels_above_threshold(parcels: list[Parcel], threshold: float) -> list:
    parcel_exceed_list = []
    for parcel in parcels:
        if parcel.area() > threshold:
            parcel_exceed_list.append(parcel.as_dict())
    return parcel_exceed_list


##########################################
# FOR EACH parcel IN parcel_list
#     IF parcel.zone A KEY OF DICT zone_parcel_dict
#         SET zone_parcel_dict[parcel.zone] = zone_parcel_dict[parcel.zone] + 1
#     ELSE
#         SET zone_parcel_dict[parcel.zone] = 1
#     END IF
# END FOR
##########################################
def count_by_zone(parcels: list[Parcel]) -> dict:
    zone_dict = {}
    for parcel in parcels:
        zone = parcel.attributes["zone"]
        if zone in zone_dict:
            zone_dict[zone] += 1
        else:
            zone_dict[zone] = 1
    return zone_dict


##########################################
# FOR EACH parcel IN parcel_list
#     IF parcel.zone IS EQUAL TO development_area_zone
#         APPEND parcel to parcel_intersect_list
#     END IF
# END FOR
##########################################
def intersecting_parcels(parcels: list[Parcel], zone) -> list:
    parcel_intersect_list = []
    for parcel in parcels:
        if parcel.attributes["zone"] == zone:
            parcel_intersect_list.append(parcel.as_dict())
    return parcel_intersect_list