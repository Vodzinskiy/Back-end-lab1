from main import app
from flask import jsonify, request
import datetime

user_id = 1
category_id = 1
note_id = 1

CATEGORIES = [
    {
        "id": category_id,
        "title": "Medicine"
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
        "date_of_creating": datetime.datetime.now()
    }
]


def validation(key, value, arr):
    for i in arr:
        if i[key] == value:
            return True
    return False


@app.route("/user", methods=["POST"])
def create_user():
    request_data = {}
    try:
        request_data["name"] = request.get_json()["name"]
        global user_id
        user_id += 1
        request_data["id"] = user_id
    except:
        return "Error bad request"
    USERS.append(request_data)
    return request_data


@app.route("/category", methods=["POST"])
def create_category():
    request_data = {}
    try:
        request_data["title"] = request.get_json()["title"]
        global category_id
        category_id += 1
        request_data["id"] = category_id
    except:
        return "Error bad request"
    CATEGORIES.append(request_data)
    return request_data


@app.route("/note", methods=["POST"])
def create_note():
    request_data = request.get_json()

    try:
        if not (validation("id", request.get_json()["user_id"], USERS) and validation("id",
                                                                                      request.get_json()["category_id"],
                                                                                      CATEGORIES)):
            return "Error, user or category is not found"
        global note_id
        note_id += 1
        request_data["id"] = note_id
        request_data["date_of_creating"] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        request_data["price"] = request.get_json()["price"]

    except:
        return "Error bad request"

    NOTES.append(request_data)
    return request_data


@app.route("/users")
def get_user():
    return jsonify({"users": USERS})


@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})


@app.route("/notes")
def get_notes():
    return jsonify({"notes": NOTES})


@app.route("/user-notes", methods=["POST"])
def get_user_notes():
    try:
        request_data = request.get_json()
        id_user = request_data["user"]
        user_notes = []
        for i in NOTES:
            if i["user_id"] == id_user:
                user_notes.append(i)
        return jsonify(user_notes)
    except:
        return "Error bad request"



@app.route("/user-category-notes", methods=["POST"])
def get_user_category_notes():
    try:
        request_data = request.get_json()
        id_user = request_data["user"]
        id_category = request_data["category"]
        user_notes = []
        for i in NOTES:
            if i["user_id"] == id_user and i["category_id"] == id_category:
                user_notes.append(i)
        return jsonify(user_notes)
    except:
        return "Error bad request"

