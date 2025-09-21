from flask import Blueprint

currency_api_blueprint = Blueprint("currency_api", __name__)
asset_api_blueprint = Blueprint("asset_api", __name__)

from . import (
    asset_routes,  # noqa: F401
    currency_routes,  # noqa: F401
)
