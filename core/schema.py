from core import ma
from core.models import CurrencyTypeEnum


class CurrencyTypeSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    name = ma.Enum(CurrencyTypeEnum, required=True)
