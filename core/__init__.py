import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

database = SQLAlchemy()


def create_app(config_type=os.getenv("CONFIG_TYPE")):
    app = Flask(__name__)

    app.config.from_object(config_type)

    initialize_extensions(app)

    return app


def initialize_extensions(app):
    database.init_app(app)
