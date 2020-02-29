import random

#Google Geolocation API
import requests
from geopy.distance import geodesic

#OpenCage Geocoder
from geopy.geocoders import OpenCage


def openAPIKey():
    with open("../key.env") as f:
        return f.read()

KEY = openAPIKey()

class City:
    '''This class retrieves coordinates from OpenCage Geocoder (or Google Geolocation API) and creates an object containing a city name, latitude and longitude '''
    
    CITIES = {}                                                         #dictionary storing already retrieved coordinates for later use

    def __init__(self, name):
        self.city = name
        if self.city not in City.CITIES:
            #OpenCage Geocoder
            geolocator = OpenCage(api_key = KEY)
            location = geolocator.geocode(self.city, timeout=6)
            if location is None:
                raise TypeError('city does not exist')
            self.latitude = location.latitude
            self.longitude = location.longitude
            City.CITIES[self.city] = (location.latitude, location.longitude)
        else:
            self.latitude = City.CITIES[self.city][0]
            self.longitude = City.CITIES[self.city][1]
            
            ##Google Geolocation API (older code)
            #resp = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(city, api_key = key))
            #print (resp.json()['results'][0]['geometry']['location']['lat'], resp.json()['results'][0]['geometry']['location']['lng'])

    def __repr__(self):
        return str(self.city)
        
    def __eq__(self, other):
        return self.city == other.city

    def __hash__(self):
        return hash(self.city)


class Tour:
    ''' This class generates a route object containing a total distance and a list of cities'''
    
    DISTANCES = {}                                                      #dictionary storing distances between two cities for later use
    
    def __init__(self, places):
        if all(isinstance(p, str) for p in places):
            self.cities = [City(place) for place in places]
        else:
            self.cities = places
        distance = 0
        for i in range(len(self.cities)-1):
            partial_distance = self.getDistance(self.cities[i], self.cities[i+1])
            distance += partial_distance
        last_distance = self.getDistance(self.cities[0], self.cities[-1])
        distance += last_distance
        fitness = 1 / float(distance)
        self.tour = (fitness, distance, self.cities)
    
    def __repr__(self):
        return str(self.tour)
        
    def __getitem__(self, index):
        return self.tour[index]
   
    def __setitem__(self, key, value):
      self.tour[key] = value
      
    def getDistance(self, city1, city2):
        ''' A method measuring distance between two cities'''
        cities = (city1, city2)
        if cities not in Tour.DISTANCES:
            latlong1 = (cities[0].latitude, cities[0].longitude)
            latlong2 = (cities[1].latitude, cities[1].longitude)
            Tour.DISTANCES[cities] = geodesic(latlong1, latlong2).kilometers
        return Tour.DISTANCES[cities]



class Population:
    '''This class generates a population of sorted tours'''
    def __init__(self, routes):
        self.population = sorted([Tour(route) for route in routes], key=lambda tup: tup[1])

    def __len__(self):
        return len(self.population)
        
    def __repr__(self):
        out = ""
        for i in self.population:
            out += str(i) + "\n"
        return out
        
    def __getitem__(self, index):
        return self.population[index]
   
    def __setitem__(self, key, value):
      self.population[key] = value

