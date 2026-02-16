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


class AssetResponseSchema(ResponseWithErrorSchema):
    id = ma.Integer()
    value = ma.Float()
    order = ma.Integer(allow_none=True)
    note = ma.String(allow_none=True)
    currency_id = ma.Integer()
    currency_code = ma.String()
    currency_name = ma.String()


class AssetPostSchema(ma.Schema):
    value = ma.Float(required=True)
    currency_id = ma.Integer(required=True)
    note = ma.String(required=False, allow_none=True)


class AssetPatchSchema(ma.Schema):
    value = ma.Float(required=False)
    currency_id = ma.Integer(required=False)
    note = ma.String(required=False, allow_none=True)
    order = ma.Integer(required=False)


class UserLoginSchema(ma.Schema):
    email = ma.String(required=True, validate=validate.Email())
    password = ma.String(required=True, validate=validate.Length(min=6))


class UserResponseSchema(ResponseWithErrorSchema):
    email = ma.String()
    uuid = ma.String(attribute="uuid")


class TokenResponseSchema(ResponseWithErrorSchema):
    token = ma.String()
