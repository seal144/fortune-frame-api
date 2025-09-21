from apifairy import body, response

from core import database
from core.models import Asset
from core.schema import AssetSchema

from . import asset_api_blueprint

asset_schema_list = AssetSchema(many=True)
asset_schema = AssetSchema()


@asset_api_blueprint.route("/assets", methods=["GET"])
@response(asset_schema_list)
def get_assets():
    return Asset.query.all()


@asset_api_blueprint.route("/assets", methods=["POST"])
@body(asset_schema)
@response(asset_schema)
def create_asset(kwargs):
    new_asset = Asset(**kwargs)
    database.session.add(new_asset)
    database.session.commit()
    return new_asset
