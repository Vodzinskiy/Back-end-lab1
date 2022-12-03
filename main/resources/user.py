from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from main.db import USERS
from main.schemas import UserSchema

blp = Blueprint("user", __name__, description="user operation")

userId = 1

@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        try:
            return USERS[user_id]
        except KeyError:
            abort(404, message="User not found")

    @blp.response(200, UserSchema)
    def delete(self, user_id):
        try:
            deleted_user = user_id
            del USERS[user_id]
            return deleted_user
        except KeyError:
            abort(404, message="User not found")


@blp.route("/user")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return list(USERS.values())

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, request_data):
        global userId
        userId += 1
        USERS[userId] = {"id": userId, "name": request_data["name"]}
        return jsonify(USERS[userId])