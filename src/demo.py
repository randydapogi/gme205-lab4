import json
from shapely.geometry import shape

from spatial import Parcel

# Using a context manager ('with') ensures the file closes automatically
with open('data/parcels.json', 'r') as file:
    parcels = json.load(file)


for parcel in parcels:
    parcel_id = parcel.pop("parcel_id")
    geometry = shape(parcel.pop("geometry"))
    attributes = parcel

    parcel = Parcel(parcel_id=101, geometry=geometry, attributes=attributes)

    print(parcel_id)
    print(geometry)
    print(attributes)
    print(parcel)
    print(parcel.area())
    print(parcel.attributes["area_sqm"])
    break