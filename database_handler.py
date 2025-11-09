import sqlite3
from database_retrieve import database_query

try:
    sqliteConnection = sqlite3.connect('Holiday_Buddies.db')
    cursor = sqliteConnection.cursor()

    print(database_query(cursor, "SELECT * FROM countries"))


except sqlite3.Error as error:
    print('Error occurred -', error)