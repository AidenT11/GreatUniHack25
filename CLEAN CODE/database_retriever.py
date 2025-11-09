import sqlite3

def database_query(cursor, query):
    try:
        # Connect to SQLite Database and create a cursor
        cursor.execute(query)

        return cursor.fetchall()

    except sqlite3.Error as error:
        return 'Error occurred - ' + str(error)