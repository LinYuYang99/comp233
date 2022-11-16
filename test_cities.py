from cities import City, CityCollection
from pathlib import Path
from utils import read_attendees_file
import csv

filepath = Path(r'C:\Users\10747\Desktop\comp233\conference\attendee_locations.csv')
collection = read_attendees_file(filepath)

print(collection.plot_top_emitters(collection.cities[0],7,True))
