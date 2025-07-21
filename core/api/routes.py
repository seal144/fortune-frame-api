from . import currency_type_api_blueprint


@currency_type_api_blueprint.route("/currency-type", methods=["GET"])
def get_currency_type():
    return "Hello, World!"
