from main import app
from flask import jsonify, request
import datetime

user_id = 1
category_id = 1
note_id = 1

CATEGORIES = [
    {
        "id": category_id,
        "name": "Medicine"
    }
]

USERS = [
    {
        "id": user_id,
        "name": "Roma",
    }
]

NOTES = [
    {
        "id": note_id,
        "user_id": user_id,
        "category_id": category_id,
        "price": 100,
        "date_of_creating": datetime.date.today()
    }
]


@app.route("/user", methods=["POST"])
def create_user():
    request_data = {}
    global user_id
    request_data["id"] = user_id + 1
    try:
        request_data["name"] = request.get_json()["name"]
    except:
        request_data["name"] = "User" + str(user_id)
    USERS.append(request_data)
    print(USERS)
    return request_data


@app.route("/users")
def get_user():
    return jsonify({"users": USERS})


@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})
