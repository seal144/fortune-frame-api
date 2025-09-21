from flask import Blueprint

currency_api_blueprint = Blueprint("currency_api", __name__)

from . import (
    currency_routes,  # noqa: F401
)
