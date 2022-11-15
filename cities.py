from typing import Dict, List, Tuple
from dataclasses import dataclass
import math

@dataclass
class City:
    def __init__(self, name: str, country: str, number: int, latitude: float, longitude: float):
       self.name=name 
       self.country=country
       self.number=number
       self.latitude=latitude
       self.longitude=longitude

    def validcity(self):
        if(self.number<0):
            return False
        if(self.latitude<-90 or self.latitude>90 or self.longitude<-180 or self.longitude>180):
            return False
        return True  

    
    def distance_to(self, other: 'City') -> float:
        x1=self.latitude
        y1=self.longitude
        x2=other.latitude
        y2=other.longitude
        d=12742*math.asin(math.sqrt(math.pow(math.sin(0.5*(x1-x2)),2)+math.cos(x1)*math.cos(x2)*math.pow(math.sin(0.5*(y1-y2)),2)))
        return d

    def co2_to(self, other: 'City') -> float:
        d=self.distance_to(other)
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
    def __init__(self, cities):
       self.cities=cities
          

    def countries(self) -> List[str]:
        countries_list = sorted([x.country for x in self.cities])
        list=[]
        a=" "
        for i in countries_list:
            if(i!=a):
                list.append(i)
                a=i
        return list

    def total_attendees(self) -> int:
        count=0
        for index in self.cities:
            count+=index.number
        return count

    def total_distance_travel_to(self, city: City) -> float:
        td=0
        for index in self.cities:
            td+=index.distance_to(city)*index.number
        return td

    def travel_by_country(self, city: City) -> Dict[str, float]:
        list1=self.countries()
        list2=[]
        for i in range (len(list1)):
            count=0.0
            for index in self.cities:
                if(index.country==list1[i]):
                    count+=index.distance_to(city)
            list2.append(count)   
        dict_tbc = dict(zip(list1, list2))
        return dict_tbc


    def total_co2(self, city: City) -> float:
        tc=0
        for index in range(1,len(self)):
            tc+=self[index].co2_to(city)
        return tc
        

    def co2_by_country(self, city: City) -> Dict[str, float]:
        list1=self.countries()
        list2=[]
        list2[0]=self[1].co2_to(city)
        for index in range(2,len(self)):
            if(self[index].country)==list2[len(list2)-1]:
               list2.append(self[index].co2_to(city))
            else:
               list2[len(list)-1]+=self[index].co2_to(city)
        dict_cbc = dict(zip(list1, list2))
        return dict_cbc

    def summary(self, city: City):
        x=int(round(self.total_co2(city)/1000,0))
        z=int(round(self.total_distance_travel_to(city),0))
        print("Host city:",city.name,"(",city.country,")")
        print("Total CO2:",x)
        print("Total attendees travelling to",city.name,"from",len(self)-1,"different cities:",z)

    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        raise NotImplementedError

    def plot_top_emitters(self, city: City, n: int, save: bool):
        raise NotImplementedError

