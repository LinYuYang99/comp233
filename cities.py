from typing import Dict, List, Tuple
from dataclasses import dataclass
import math

@dataclass
class City:
    def __init__(self, name: str, state: str, country: str, number: int, latitude: float, longitude: float):
       self.name=name 
       self.state=state 
       self.country=country
       self.number=number
       self.latitude=latitude
       self.longitude=longitude

    
    def distance_to(self, other: 'City') -> float:
        x1=self.latitude
        y1=self.longitude
        x2=other.latitude
        y2=other.longitude
        d=12742*math.asin(math.sqrt(math.pow(math.sin(0.5*(x1-x2)),2)+math.cos(x1)*math.cos(x2)*math.pow(math.sin(0.5*(y1-y2)),2)))
        return d

    def co2_to(self, other: 'City') -> float:
        x1=self.latitude
        y1=self.longitude
        x2=other.latitude
        y2=other.longitude
        d=12742*math.asin(math.sqrt(math.pow(math.sin(0.5*(x1-x2)),2)+math.cos(x1)*math.cos(x2)*math.pow(math.sin(0.5*(y1-y2)),2)))
        co2=0
        if(d<=1000):
            co2=200*d*self.number
        elif(d<=8000):
            co2=250*d*self.number
        else:
            co2=300*d*self.number

        return co2

        

@dataclass
class CityCollection:
    ...

    def countries(self) -> List[str]:
        raise NotImplementedError

    def total_attendees(self) -> int:
        raise NotImplementedError

    def total_distance_travel_to(self, city: City) -> float:
        raise NotImplementedError

    def travel_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def total_co2(self, city: City) -> float:
        raise NotImplementedError

    def co2_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def summary(self, city: City):
        raise NotImplementedError

    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        raise NotImplementedError

    def plot_top_emitters(self, city: City, n: int, save: bool):
        raise NotImplementedError

