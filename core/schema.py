from core import ma
from core.models import CurrencyTypeEnum


# only get needed for the currencies
class CurrencyGetSchema(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    code = ma.String()
    currency_type = ma.Enum(CurrencyTypeEnum, attribute="currency_type_rel.name")
    multiplier = ma.Float()
    parent = ma.Integer()


class AssetSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    value = ma.Float(required=True)
    order = ma.Integer(allow_none=True)
    currency = ma.Integer(required=True)
    note = ma.String(allow_none=True)
    currency_code = ma.String(dump_only=True)


class AssetPatchSchema(ma.Schema):
    value = ma.Float(required=False)
    order = ma.Integer(required=False)
    currency = ma.Integer(required=False)
    note = ma.String(required=False, allow_none=True)
