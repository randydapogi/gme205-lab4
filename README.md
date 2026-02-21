# GmE 205 – Laboratory Exercise 4

## Overview

GmE 205 Lab Exercise 4

---

## Environment Setup

- Python 3.x

---

## How to Run

1. Activate the virtual environment

---

## Outputs

---

## Algorithm

1. Start
2. Load parcel data from JSON file
3. Convert each record into a Parcel object
4. Set the development boundary
5. Set the theshold value
6. If no parcels are loaded:

- Display error message
- Stop program

7. Initialize:

- total_active_area to zero
- parcel_exceed_list to an empty list
- zone_parcel_dict to an empty dictionary
- parcel_intersect_list to an empty list

8. Loop over all parcels
9. For each parcel

- if parcel is active, add parcel area to total_active_area
- if parcel area is greater than threshold, add parcel to parcel_exceed_list
- if parcel zone is not in zone_parcel_dict, add key value pair in dict with parcel zone being the key and 0 being the value, else increament by 1 the value of dictionary with key of parcel zone
- if parcel geometry intersects with development boundary, add parcel to parcel_intersect_list

10. Total area of all active parcels is in total_active_area
11. The parcels that exceeded the threshold are in parcel_exceed_list
12. zone_parcel_dict contains the dictionary with key value pair of the zone and its parcel count
13. The parcels that intersect the proposed development boundary are in parcel_intersect_list

---

## Pseudocode

```
BEGIN
  LOAD parcel_data from JSON file
  CONVERT parcel_data into Parcel objects
  STORE in parcel_list

  GET THRESHOLD AND STORE TO threshold
  GET DEVELOPMENT BOUNDARY AND STORE TO development_boundary

  IF parcel_list is empty THEN
    PRINT "No parcels found."
    STOP
  END IF

  SET total_active_area = 0
  SET parcel_exceed_list = []
  SET zone_parcel_dict = {}
  SET parcel_intersect_list = []

  FOR EACH parcel IN parcel_list
    IF parcel.active is TRUE
      total_active_area = total_active_area + parcel.area
    END IF

    IF parcel.area > threshold
      APPEND parcel to parcel_exceed_list
    END IF

    IF parcel.zone A KEY OF DICT zone_parcel_dict
      SET zone_parcel_dict[parcel.zone] = zone_parcel_dict[parcel.zone] + 1
    ELSE
      SET zone_parcel_dict[parcel.zone] = 0
    END IF

    IF parcel.geometry INTERSECT WITH development_boundary
      APPEND parcel to parcel_intersect_list
    END IF
  END FOR

  DISPLAY total_active_area AS TOTAL AREA OF ALL ACTIVE PARCEL
  DISPLAY parcel_exceed_list AS LIST OF PARCELS THAT EXCEED THE THRESHOLD
  DISPLAY zone_parcel_dict AS DICT KEY VALUE PAIR OF ZONE AND PARCEL COUNT OF THAT ZONE
  DISPLAY parcel_intersect_list AS LIST OF PARCELS THAT INTERSECT WITH THE DEVELOPMENT BOUNDARY
END
```

---

## Reflection

---
