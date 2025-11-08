import sqlite3

try:
    # Connect to SQLite Database and create a cursor
    sqliteConnection = sqlite3.connect('users.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    # Execute a query to get the SQLite version
    query = 'SELECT * FROM users;'
    cursor.execute(query)

    # Fetch and print the result
    result = cursor.fetchall()
    print(result)

    # Close the cursor after use
    cursor.close()

except sqlite3.Error as error:
    print('Error occurred -', error)