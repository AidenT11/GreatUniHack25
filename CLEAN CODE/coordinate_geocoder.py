from geopy.geocoders import Nominatim
from airport_finder import csv_search
import os

def geocode_coords(area1, area2):
    geolocator = Nominatim(user_agent="Holiday Buddies")

    location1 = geolocator.geocode(area1)

    location2 = geolocator.geocode(area2)

    return location1, location2

def find_airport(location1, location2):
    midpoint_latitude = (location1.latitude + location2.latitude) / 2
    midpoint_longitude = (location1.longitude + location2.longitude) / 2
    return csv_search("airports.csv", midpoint_latitude, midpoint_longitude)