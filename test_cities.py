from cities import City, CityCollection
from pathlib import Path
from utils import read_attendees_file
import csv

filepath = Path(r'C:\Users\10747\Desktop\comp233\conference\attendee_locations.csv')
collection = read_attendees_file(filepath)


def test_distance(self,other):
    self.distance_to(other)

def test_CityCollection(self,other):
    print(self)

def test_hostcity(self,other):
    print(collection.plot_top_emitters(collection.cities[0],7,True))

def test_sorted_by_emissions(self):
    print(self.sorted_by_emissions())