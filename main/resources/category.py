from flask_smorest import Blueprint, abort
from flask.views import MethodView
from main.db import CATEGORIES
from flask import request, jsonify

from main.schemas import CategorySchema

blp = Blueprint("category", __name__, description="category operation")

categoryId = 1

@blp.route("/category/<int:category_id>")
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, category_id):
        try:
            return CATEGORIES[category_id]
        except KeyError:
            abort(404, message="Category not found")

    @blp.response(200, CategorySchema)
    def delete(self, category_id):
        try:
            deleted_category = CATEGORIES[category_id]
            del CATEGORIES[category_id]
            return deleted_category
        except KeyError:
            abort(404, message="Category not found")


@blp.route("/category")
class CategoryList(MethodView):

    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return list(CATEGORIES.values())

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, request_data):
        global categoryId
        categoryId += 1
        CATEGORIES[categoryId] = {"id": categoryId, "title": request_data["title"]}
        return jsonify(CATEGORIES[categoryId])
