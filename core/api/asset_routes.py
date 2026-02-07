from apifairy import body, response
from flask import g

from core import database
from core.auth import require_auth
from core.models import Asset
from core.schema import AssetPatchSchema, AssetSchema

from . import asset_api_blueprint

asset_schema_list = AssetSchema(many=True)
asset_schema = AssetSchema()
asset_patch_schema = AssetPatchSchema()


@asset_api_blueprint.route("/assets", methods=["GET"])
@require_auth
@response(asset_schema_list)
def get_assets():
    return Asset.query.filter_by(user_id=g.current_user.id).all()


@asset_api_blueprint.route("/assets", methods=["POST"])
@require_auth
@body(asset_schema)
@response(asset_schema)
def create_asset(kwargs):
    new_asset = Asset(**kwargs, user_id=g.current_user.id)
    database.session.add(new_asset)
    database.session.commit()
    return new_asset


@asset_api_blueprint.route("/assets/<int:asset_id>", methods=["PATCH"])
@require_auth
@body(asset_patch_schema)
@response(asset_schema)
def patch_asset(kwargs, asset_id):
    # TODO - add custom error handling after FE implementation
    asset = Asset.query.filter_by(id=asset_id, user_id=g.current_user.id).first_or_404()
    for key, value in kwargs.items():
        setattr(asset, key, value)
    database.session.commit()
    return asset


@asset_api_blueprint.route("/assets/<int:asset_id>", methods=["DELETE"])
@require_auth
@response(asset_schema)
def delete_asset(asset_id):
    # TODO - add custom error handling after FE implementation
    asset = Asset.query.filter_by(id=asset_id, user_id=g.current_user.id).first_or_404()
    database.session.delete(asset)
    database.session.commit()
    return asset
