import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def create_app(config_type=os.getenv("CONFIG_TYPE")):
    app = Flask(__name__)

    app.config.from_object(config_type)

    return app
