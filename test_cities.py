from cities import City, CityCollection
from pathlib import Path
from utils import read_attendees_file
import csv

filepath = Path(r'C:\Users\10747\Desktop\comp233\comp233\attendee_locations.csv')
collection = read_attendees_file(filepath)

Algiers=City(collection[1][3],collection[1][2],collection[1][1],int(collection[1][0]),float(collection[1][4]),float(collection[1][5]))
Córdoba=City(collection[3][3],collection[3][2],collection[3][1],int(collection[3][0]),float(collection[3][4]),float(collection[3][5]))
a=Algiers.distance_to(Córdoba)
print(a)
print(Algiers.name)
print(Córdoba)

