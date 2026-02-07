from apifairy import body, response
from flask import g
from werkzeug.security import check_password_hash, generate_password_hash

from core import database
from core.auth import generate_token, require_auth
from core.models import User
from core.schema import (
    TokenResponseSchema,
    UserLoginSchema,
    UserResponseSchema,
)

from . import auth_api_blueprint

user_login_schema = UserLoginSchema()
user_response_schema = UserResponseSchema()
token_response_schema = TokenResponseSchema()


@auth_api_blueprint.route("/auth/register", methods=["POST"])
@body(user_login_schema)
@response(token_response_schema, 201)
def register(kwargs):
    """Register a new user account."""
    email = kwargs.get("email")
    password = kwargs.get("password")

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return {"error": "email_already_registered"}, 409

    password_hash = generate_password_hash(password)
    new_user = User(
        email=email,
        password_hash=password_hash,
    )

    database.session.add(new_user)
    database.session.commit()

    token = generate_token(new_user.id, new_user.email)

    return {
        "token": token,
    }


@auth_api_blueprint.route("/auth/login", methods=["POST"])
@body(user_login_schema)
@response(token_response_schema)
def login(kwargs):
    """Authenticate user and return JWT token."""
    email = kwargs.get("email")
    password = kwargs.get("password")

    user = User.query.filter_by(email=email).first()
    if not user:
        return {"error": "invalid_email_or_password"}, 401

    if not check_password_hash(user.password_hash, password):
        return {"error": "invalid_email_or_password"}, 401

    token = generate_token(user.id, user.email)

    return {
        "token": token,
    }


@auth_api_blueprint.route("/auth/me", methods=["GET"])
@require_auth
@response(user_response_schema)
def get_current_user():
    """Get current authenticated user information."""
    return g.current_user
