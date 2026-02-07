from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import current_app, g, request

from core.models import User


def generate_token(user_id, email):
    """Generate a JWT token for a user."""
    app = current_app
    payload = {
        "user_id": user_id,
        "email": email,
        "exp": datetime.utcnow()
        + timedelta(seconds=app.config["JWT_EXPIRATION_DELTA"]),
        "iat": datetime.utcnow(),
    }
    token = jwt.encode(
        payload,
        app.config["JWT_SECRET_KEY"],
        algorithm=app.config["JWT_ALGORITHM"],
    )
    return token


def verify_token(token):
    """Verify a JWT token and return the payload if valid."""
    try:
        app = current_app
        payload = jwt.decode(
            token,
            app.config["JWT_SECRET_KEY"],
            algorithms=[app.config["JWT_ALGORITHM"]],
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def get_token_from_header():
    """Extract JWT token from Authorization header."""
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None

    try:
        # Expected format: "Bearer <token>"
        token_type, token = auth_header.split(" ", 1)
        if token_type.lower() != "bearer":
            return None
        return token
    except ValueError:
        return None


def require_auth(f):
    """Decorator to require authentication for a route."""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = get_token_from_header()

        if not token:
            return {"error": "Authentication required"}, 401

        payload = verify_token(token)
        if not payload:
            return {"error": "Invalid or expired token"}, 401

        # Load user from database and attach to request context
        user = User.query.get(payload["user_id"])
        if not user:
            return {"error": "User not found"}, 401

        g.current_user = user
        return f(*args, **kwargs)

    return decorated_function
