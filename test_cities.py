from cities import City, CityCollection
from pathlib import Path
from utils import read_attendees_file
import csv

filepath = Path(r'C:\Users\10747\Desktop\comp233\comp233\attendee_locations.csv')
collection = read_attendees_file(filepath)

zurich = City('Zurich', 'United States', 52, 47.22, 8.33)
san_francisco = City('San Francisco', 'United States', 71, 37.77, -122.41)
greenwich = City('London', 'United Kingdom', 15, 51.48, 0)
list_of_cities = [zurich, san_francisco, greenwich]
city_collection = CityCollection(list_of_cities)
print(city_collection.countries())


