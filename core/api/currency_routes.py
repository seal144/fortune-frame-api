from apifairy import response

from core.models import Currency
from core.schema import CurrencyGetSchema

from . import currency_api_blueprint

currency_schema = CurrencyGetSchema(many=True)


@currency_api_blueprint.route("/currencies", methods=["GET"])
@response(currency_schema)
def get_currencies():
    return Currency.query.all()
