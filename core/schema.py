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
