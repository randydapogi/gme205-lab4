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
4. If no parcels are loaded:

- Display error message
- Stop program

5. Set the development area zone
6. Set the theshold value
7. Initialize:

- total_active_area to zero
- parcel_exceed_list to an empty list
- zone_parcel_dict to an empty dictionary
- parcel_intersect_list to an empty list

8. Loop over all parcels
9. For each parcel

- if parcel is active, add parcel area to total_active_area
- if parcel area is greater than threshold, add parcel to parcel_exceed_list
- if parcel zone is not in zone_parcel_dict, add key value pair in dict with parcel zone being the key and 1 being the value, else increament by 1 the value of dictionary with key of parcel zone
- if parcel zone is equal to development area zone, add parcel to parcel_intersect_list

10. Total area of all active parcels is in total_active_area
11. The parcels that exceeded the threshold are in parcel_exceed_list
12. zone_parcel_dict contains the dictionary with key value pair of the zone and its parcel count
13. The parcels with zone equal to the development area zone are in parcel_intersect_list
14. Save output into json file

---

## Pseudocode

```
BEGIN
  LOAD parcel_data from JSON file
  CONVERT parcel_data into Parcel objects
  STORE in parcel_list

  IF parcel_list is empty THEN
    PRINT "No parcels found."
    STOP
  END IF

  GET THRESHOLD AND STORE TO threshold
  GET DEVELOPMENT AREA ZONE AND STORE TO development_area_zone

  SET active_area = 0
  SET parcel_exceed_list = []
  SET zone_parcel_dict = {}
  SET parcel_intersect_list = []

  FOR EACH parcel IN parcel_list
    IF parcel.active is TRUE
      active_area = active_area + parcel.area
    END IF

    IF parcel.area > threshold
      APPEND parcel to parcel_exceed_list
    END IF

    IF parcel.zone A KEY OF DICT zone_parcel_dict
      SET zone_parcel_dict[parcel.zone] = zone_parcel_dict[parcel.zone] + 1
    ELSE
      SET zone_parcel_dict[parcel.zone] = 1
    END IF

    IF parcel.zone IS EQUAL TO development_area_zone
      APPEND parcel to parcel_intersect_list
    END IF
  END FOR

  DISPLAY active_area AS TOTAL AREA OF ALL ACTIVE PARCEL
  DISPLAY parcel_exceed_list AS LIST OF PARCELS THAT EXCEED THE THRESHOLD
  DISPLAY zone_parcel_dict AS DICT KEY VALUE PAIR OF ZONE AND PARCEL COUNT OF THAT ZONE
  DISPLAY parcel_intersect_list AS LIST OF PARCELS WITH ZONE EQUAL TO DEVELOPMENT AREA ZONE

  SAVE OUTPUT TO JSON FILE
END
```

---

## Reflection

1. Where in your system do Sequence, Selection, and Repetition explicitly appear?

- Sequence structure explicitly appear in run_lab4.py.
- Selection and Repetition structure explicitly appear on the functions in analysis.py altho there are also Select structure in the check if parcel list is empty in run_lab4.py and there are Repeatition structure in the convertion of parcel from the list of dict to a list of Parcel objects in the run_lab4.py

2. If you removed your algorithm planning step, how would your implementation likely change?

- I i removed my algorithm planning step, I would most probaly start by writing code in the run_lab4.py and writing the needed functions and methods in the spatial.py and analysis.py as needed. When I wrote the algorithm first, I was able to see the needed methods and functions needed by the system in advanced therefore I wrote the needed methods and functions in the spatial.py and analysis.py first before writing the script that will execute the requirements in run_lab4.py

3. Where does spatial behavior live in your system, and why is that important?

- Spatial behaviour lives in the SpatialObject class. This makes undestanding how the system handles spatial behaviour easier since it is in one place. This also makes changing algorithms or libraries used for the spatial behaviour easier.

4. Why does analysis.py contain structured logic instead of demo.py?

- Placing the structured logic in analysis.py instead of demo.py/run_lab4.py makes it so that the structured logic can be used by other scripts aside from the demo.py/run_lab4.py script. This also makes it so that the execution of the functions in the analysis.py is abstracted to the run_lab4.py script. The script just needs to know the input parameter of the functions and the output of the functions.

5. What would happen if all filtering logic were placed inside the Parcel class?

- If all filtering logic were placed inside the Parcel class, the script will still work however this would make the Parcel class have more responsibilities. This responsibilities would not be might not be generally used by other scripts using the Parcel class therefore it is better to separate this logic from the Parcel class.

6. If a new rule is added (e.g., “exclude inactive industrial parcels”), how easily can your current design adapt?

- In my current design to implement “exclude inactive industrial parcels” we just need to add a new function in the analysis.py and call that function and add the output in the summary dict in the run_lab4.py. This changes will not affect the other parts of the code.

7. How does separating structured logic from object behavior prevent “God classes”?

- Separationg structured logic from the Object class makes it so that the object class does not have all the responsibilities. This makes it so that any change in the structured logic will not affect the object class therefore not affecting the other scripts using the object class.

---
