from flask import MethodView
from flask_smorest import Blueprint, abort
from flask import request, jsonify

from main.db import USERS

blp = Blueprint("currency", __name__, description="user operation")


@blp.route("/user/<int:user_id>")
class User(MethodView):
    def get(self, user_id):
        try:
            return USERS[user_id]
        except KeyError:
            abort(404, message="User not found")


    def delete(self, user_id):
        try:
            deleted_user = user_id
            del USERS[user_id]
            return deleted_user
        except KeyError:
            abort(404, message="User not found")


@blp.route("/user")
class UserList(MethodView):
    def get(self):
        return USERS

    def post(self):
        request_data = {}
        global userId
        try:
            userId += 1
            request_data["id"] = userId
            request_data["name"] = request.get_json()["name"]
        except:
            return "Error bad request"
        USERS[userId] = request_data
        return jsonify(request_data)

