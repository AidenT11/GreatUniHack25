from flask import Flask, request, jsonify
from flask_cors import CORS  # import CORS
import sqlite3
from create_user import add_user
from database_retriever import database_query
from search_users import search_compatable_users

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # only allow React dev server

# --- Add user ---
@app.route("/api/add_user", methods=["POST"])
def api_add_user():
    data = request.get_json()
    try:
        conn = sqlite3.connect("Holiday_Buddy.db")
        cursor = conn.cursor()

        result = add_user(
            cursor,
            username=data["username"],
            password=data["password"],
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            country=data.get("country", "France"),
            city=data.get("city", "Paris")
        )

        user_id = list(database_query(cursor, "SELECT MAX(user_id) FROM user_info")[0])[0]

        conn.commit()
        conn.close()

        return jsonify({"status": "success", "message": result, "user_id": user_id})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


# --- Match user ---
@app.route("/api/match_user/<int:user_id>", methods=["GET"])
def api_match_user(user_id):
    try:
        conn = sqlite3.connect("Holiday_Buddy.db")
        cursor = conn.cursor()

        soulmate_id = search_compatable_users(cursor, user_id)
        if soulmate_id == "No matches":
            soulmate_id = user_id + 1

        data = database_query(cursor, f"""
            SELECT name, age, country, city
            FROM user_info
            WHERE user_id = {soulmate_id}
        """)[0]

        name, age, country, city = data


        conn.close()

        return jsonify({
            "id": soulmate_id,
            "name": name,
            "age": age,
            "country": country,
            "city": city,
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
