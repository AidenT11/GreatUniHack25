from geopy.geocoders import Nominatim
import math
from airport_search import csv_search

geolocator = Nominatim(user_agent="Holiday Buddies")

location1 = geolocator.geocode("England, Manchester")

location2 = geolocator.geocode("Japan, Fukushima")

print((location1.latitude + location2.latitude) / 2, (location1.longitude + location2.longitude) / 2)

print(csv_search("airports.csv", (location1.latitude + location2.latitude) / 2, (location1.longitude + location2.longitude) / 2))