from sqlalchemy.exc import IntegrityError
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.orm.exc import UnmappedInstanceError

from main.db import db

from main.models import CategoryModel
from main.schemas import CategorySchema

blp = Blueprint("category", __name__, description="category operation")


@blp.route("/category/<int:category_id>")
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, category_id):
        return CategoryModel.query.get_or_404(category_id)

    @blp.response(200, CategorySchema)
    def delete(self, category_id):
        try:
            category = CategoryModel.query.get(category_id)
            db.session.delete(category)
            db.session.commit()
            return category
        except UnmappedInstanceError:
            abort(404, "Category not found")


@blp.route("/category")
class CategoryList(MethodView):

    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, request_data):
        category = CategoryModel(**request_data)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(400, "Category with this name already exists")
        return category
