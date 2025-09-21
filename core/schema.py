from core import ma
from core.models import CurrencyTypeEnum


class CurrencyTypeSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    name = ma.Enum(CurrencyTypeEnum, required=True)


# only get needed for currencies
class CurrencyGetSchema(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    code = ma.String()
    currency_type = ma.Enum(CurrencyTypeEnum, attribute="currency_type_rel.name")
    multiplier = ma.Float()
    parent = ma.Integer()
