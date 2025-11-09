import sqlite3
from database_retriever import database_query
from coordinate_geocoder import geocode_coords, find_airport

try:
    sqliteConnection = sqlite3.connect('Holiday_Buddies.db')
    cursor = sqliteConnection.cursor()

    area1 = "France, Paris"
    area2 = "Japan, Fukushima"

    location1, location2 = geocode_coords(area1, area2)

    print(find_airport(location1, location2))


except sqlite3.Error as error:
    print('Error occurred -', error)