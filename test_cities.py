from cities import City, CityCollection
from pathlib import Path
from utils import read_attendees_file
import csv
import pytest

filepath = Path(r'C:\Users\10747\Desktop\comp233\conference\attendee_locations.csv')
collection = read_attendees_file(filepath)


def test_distance():
    exp_error_lon_number = "invalid longitude"
    exp_error_att_number = "invalid attendance number"
    exp_error_lat_number = "invalid longitude"
    with pytest.raises(AssertionError, match=exp_error_lon_number):
        city = City('Zurich', 'Switzerland' , 52, 47.22, 360)
    with pytest.raises(AssertionError, match=exp_error_att_number):
        city = City('Zurich', 'Switzerland' , -5, 47.22, 140)
    with pytest.raises(AssertionError, match=exp_error_lat_number):
        city = City('Zurich', 'Switzerland' , 52, 100, 50)

def test_CityCollection():
    raise NotImplementedError

def test_hostcity():
    raise NotImplementedError

def test_sorted_by_emissions():
    raise NotImplementedError