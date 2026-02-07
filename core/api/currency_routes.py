from apifairy import response

from core.auth import require_auth
from core.models import Currency
from core.schema import CurrencyResponseSchema

from . import currency_api_blueprint

currency_response_schema_list = CurrencyResponseSchema(many=True)


@currency_api_blueprint.route("/currencies", methods=["GET"])
@require_auth
@response(currency_response_schema_list)
def get_currencies():
    return Currency.query.all()
