from flask import Blueprint

currency_type_api_blueprint = Blueprint("currency_type_api", __name__)

from . import currency_type_routes  # noqa: F401
