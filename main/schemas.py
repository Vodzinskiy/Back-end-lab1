from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class NoteSchema(Schema):
    id = fields.Str(dump_only=True)
    user_id = fields.Str(required=True)
    category_id = fields.Str(required=True)
    price = fields.Float(required=True)


class NoteQuerySchema(Schema):
    user_id = fields.Int(required=True)
    category_id = fields.Int()
