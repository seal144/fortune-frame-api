from marshmallow import validate

from core import ma
from core.models import CurrencyTypeEnum


class ResponseWithErrorSchema(ma.Schema):
    error = ma.String(allow_none=True)


class CurrencyResponseSchema(ResponseWithErrorSchema):
    id = ma.Integer()
    name = ma.String()
    code = ma.String()
    currency_type = ma.Enum(CurrencyTypeEnum, attribute="currency_type_rel.name")
    multiplier = ma.Float()
    parent = ma.Integer()


# TODO - crete different schem a for asset post and response, and update other schemas to be splitted and uses the ResponseWithErrorSchema as base if needed (all routes that require auth can have error field)
# TODO - add currency id to the asset schema
class AssetSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    value = ma.Float(required=True)
    order = ma.Integer(allow_none=True)
    note = ma.String(allow_none=True)
    currency_code = ma.String(dump_only=True)
    currency_name = ma.String(dump_only=True)


class AssetPatchSchema(ma.Schema):
    value = ma.Float(required=False)
    order = ma.Integer(required=False)
    currency = ma.Integer(required=False)
    note = ma.String(required=False, allow_none=True)


class UserLoginSchema(ma.Schema):
    email = ma.String(required=True, validate=validate.Email())
    password = ma.String(required=True, validate=validate.Length(min=6))


class UserResponseSchema(ResponseWithErrorSchema):
    email = ma.String()
    uuid = ma.String(attribute="uuid")


class TokenResponseSchema(ResponseWithErrorSchema):
    token = ma.String()
