import csv
from pathlib import Path

from cities import City, CityCollection


def isint(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

def isfloat(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

def read_attendees_file(filepath) -> CityCollection:
    with open(filepath, newline='') as csvfile:
     spamreader = csv.reader(csvfile)
     a = [row for row in spamreader]
     c=[]
    for i in range (len(a)):
      if(isint(a[i][0]) and isfloat(a[i][4]) and isfloat(a[i][5])):
        b=City(a[i][3],a[i][1],int(a[i][0]),float(a[i][4]),float(a[i][5]))
        if(b.validcity()):
           c.append(b)
    city_collection = CityCollection(c)      
    return city_collection

filepath = Path("attendee_locations.csv")
collection = read_attendees_file(filepath)

