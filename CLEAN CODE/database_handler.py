import sqlite3
from database_retriever import database_query
from coordinate_geocoder import geocode_coords, find_airport

try:
    sqliteConnection = sqlite3.connect('Holiday_Buddies.db')
    cursor = sqliteConnection.cursor()

    username1 = 'noah'
    username2 = 'kevin'

    person1_location = ", ".join(database_query(cursor, "SELECT COUNTRY, CITY FROM user_info WHERE name ='"+username1+"'")[0])
    person2_location = ", ".join(database_query(cursor, "SELECT COUNTRY, CITY FROM user_info WHERE name = '"+username2+"'")[0])

    location1, location2 = geocode_coords(person1_location, person2_location)

    print(find_airport(location1, location2))


except sqlite3.Error as error:
    print('Error occurred -', error)