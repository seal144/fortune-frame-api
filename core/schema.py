from core import ma


class CurrencyTypeSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
