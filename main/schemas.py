from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    currency = fields.Str(required=False, missing="UAH")


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)


class NoteQuerySchema(Schema):
    user_id = fields.Int(required=True)
    category_id = fields.Int()


class NoteSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    price = fields.Float(required=True)
    currency_title = fields.Str(required=False, missing=None)


class CurrencySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)