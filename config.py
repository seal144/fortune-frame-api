import os

from sqlalchemy.engine.url import URL

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    FLASK_ENV = os.getenv("FLASK_ENV")


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


class ProductionConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
