import sqlite3
from database_retriever import database_query
from database_pusher import database_add

def add_user(cursor, username, password, name, age, gender, country, city):
    try:
        user_id = list(database_query(cursor, "SELECT COUNT(*) FROM users")[0])[0] + 1

        statement = "INSERT INTO users (username, password)" \
        "VALUES" \
        "('"+str(username)+"', '"+str(password)+"');"

        database_add(cursor, statement)


        statement = "INSERT INTO user_info (user_id, name, age, gender, country, city)" \
        "VALUES" \
        "("+str(user_id)+", '"+str(name)+"', "+str(age)+", '"+str(gender)+"', '"+str(country)+"', '"+str(city)+"');"


        database_add(cursor, statement)

        return "User added"

    except sqlite3.Error as error:
        return ('Error occurred -', error)