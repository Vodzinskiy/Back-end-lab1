import datetime

user_id = 1
category_id = 1
note_id = 1

CATEGORIES = {
    category_id:
    {
        "id": category_id,
        "title": "Medicine"
    }
}

USERS = {
    user_id:
    {
        "id": user_id,
        "name": "Roma",
    }
}

NOTES = {
    note_id:
    {
        "id": note_id,
        "user_id": user_id,
        "category_id": category_id,
        "price": 100,
        "date_of_creating": datetime.datetime.now()
    }
}

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()