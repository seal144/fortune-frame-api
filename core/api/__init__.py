from flask import Blueprint

currency_type_api_blueprint = Blueprint("currency_type_api", __name__)
currency_api_blueprint = Blueprint("currency_api", __name__)

from . import (
    currency_routes,  # noqa: F401
    currency_type_routes,  # noqa: F401
)
