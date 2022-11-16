from typing import Dict, List, Tuple
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt


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
        x1=math.radian(self.latitude)
        y1=math.radian(self.longitude)
        x2=math.radian(other.latitude)
        y2=math.radian(other.longitude)
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
                    count+=index.distance_to(city)*index.number
            list2.append(count)   
        dict_tbc = dict(zip(list1, list2))
        return dict_tbc


    def total_co2(self, city: City) -> float:
        tc=0
        for index in self.cities:
            tc+=index.co2_to(city)*index.number
        return tc
        

    def co2_by_country(self, city: City) -> Dict[str, float]:
        list1=self.countries()
        list2=[]
        for i in range (len(list1)):
            count=0.0
            for index in self.cities:
                if(index.country==list1[i]):
                    count+=index.co2_to(city)*index.number
            list2.append(count)
        dict_cbc = dict(zip(list1, list2))
        return dict_cbc

    def summary(self, city: City):
        list1=self.countries()
        x=int(round(self.total_co2(city)/1000,0))
        z=int(round(self.total_distance_travel_to(city),0))
        print("Host city:",city.name,"(",city.country,")")
        print("Total CO2:",x," tonnes")
        print("Total attendees travelling to",city.name,"from",len(list1),"different cities:",z)

    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        list3=[]
        for index in self.cities:
            a=index.name
            b=self.total_co2(index)
            list3.append([a,b])
        list4=sorted(list3, key=lambda s: s[1])
        list5=[]
        for index in range(len(self.cities)):
            a=list4[index][0]
            b=list4[index][1]
            list5.append((a,b))
        
        return list5      
        

    def plot_top_emitters(self, city: City, n: int, save: bool):
        list1=self.countries()
        list2=[]
        for i in range (len(list1)):
            count=0.0
            for index in self.cities:
                if(index.country==list1[i]):
                    count+=index.co2_to(city)*index.number
            list2.append([list1[i],count])
        list7=sorted(list2, key=lambda s: s[1],reverse=True)
        for index in range (n,len(list2)):
            list7[n][1]+=list7[index][1]
        list7[n][0]="All other countries"
        s='total emissions from each country for top '
        s+=str(n)
        plt.title(s)
        plt.ylabel('total emissions (tonnes CO2)')
        for index in range (n+1):
            plt.bar(list7[index][0],list7[index][1]/1000)        
        a=city.name
        b = a.casefold()
        return plt.show()

