from apifairy import response

from core.schema import CurrencyTypeSchema

from . import currency_type_api_blueprint

currency_type_schema = CurrencyTypeSchema(many=True)


@currency_type_api_blueprint.route("/currency-type", methods=["GET"])
@response(currency_type_schema)
def get_currency_type():
    pass
