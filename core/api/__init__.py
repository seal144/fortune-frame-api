from flask import Blueprint

currency_type_api_blueprint = Blueprint("currency_type_api", __name__)

from . import routes  # noqa: F401
