from sqlalchemy.exc import IntegrityError
from flask.views import MethodView
from flask_smorest import Blueprint
from flask import abort
from sqlalchemy.orm.exc import UnmappedInstanceError

from main.db import db
from main.models import CurrencyModel
from main.schemas import UserSchema
from main.models.user import UserModel

blp = Blueprint("user", __name__, description="user operation")


@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        return UserModel.query.get_or_404(user_id)

    @blp.response(200, UserSchema)
    def delete(self, user_id):
        try:
            user = UserModel.query.get(user_id)
            db.session.delete(user)
            db.session.commit()
            return user
        except UnmappedInstanceError:
            abort(404, "User not found")


@blp.route("/user")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, request_data):
        if not (bool(CurrencyModel.query.filter_by(title=request_data["currency"]).first())):
            abort(code=404, description="Currency not found")
        user = UserModel(**request_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, "User with this name already exists")
        return user
