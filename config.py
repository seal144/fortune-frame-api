import os

from sqlalchemy.engine.url import URL

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    FLASK_ENV = os.getenv("FLASK_ENV")

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", os.getenv("SECRET_KEY"))
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_DELTA = 30 * 24 * 60 * 60  # 30 days in seconds


class DevelopmentConfig(Config):
    DEBUG = True

    url_object = URL.create(
        "postgresql+psycopg2",
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
    )

    SQLALCHEMY_DATABASE_URI = url_object

    APIFAIRY_TITLE = "Fortune Frame API"
    APIFAIRY_UI = "/swagger_ui"
    APIFAIRY_VERSION = "1.0.0"

    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")


class ProductionConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False

    # TODO - set production SQLALCHEMY_DATABASE_URI

    CORS_ORIGINS = os.getenv("CORS_ORIGINS")
