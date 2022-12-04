from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.orm.exc import UnmappedInstanceError

from main.db import db
from sqlalchemy.exc import IntegrityError
from main.models import NoteModel

from main.schemas import NoteSchema, NoteQuerySchema

blp = Blueprint("note", __name__, description="note operation")


@blp.route("/note/<int:note_id>")
class Note(MethodView):
    @blp.response(200, NoteSchema)
    def get(self, note_id):
        return NoteModel.query.get_or_404(note_id)

    @blp.response(200, NoteSchema)
    def delete(self, note_id):
        try:
            note = NoteModel.query.get(note_id)
            db.session.delete(note)
            db.session.commit()
            return note
        except UnmappedInstanceError:
            abort(404, "Note not found")


@blp.route("/note")
class NoteList(MethodView):
    @blp.arguments(NoteQuerySchema, location="query", as_kwargs=True)
    @blp.response(200, NoteSchema(many=True))
    def get(self, **kwargs):
        try:
            user_id = int(kwargs.get("user_id"))
            print(user_id)
            query = NoteModel.query.filter(user_id == user_id)
            try:
                category_id = int(kwargs.get("category_id"))
                query = NoteModel.query.filter(category_id == category_id)
                return query.all()
            except TypeError:
                return query.all()
        except KeyError:
            abort(400, message="Missing user_id")

    @blp.arguments(NoteSchema)
    @blp.response(200, NoteSchema)
    def post(self, request_data):
        try:
            request_data["currency_id"]
        except KeyError:
            request_data["currency_id"] = 1
        note = NoteModel(**request_data)
        try:
            db.session.add(note)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Error bad request")
        return note