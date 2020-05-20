from utils import CustomJSONEncoder
from utils.models.games import db
import loader.config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import logging
import os

# db = SQLAlchemy()

logging.basicConfig(
    format="%(asctime)s %(name)-8s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)


def create_app(config_class="loader.config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(os.environ.get("FLASK_ENV") or config_class)
    app.json_encoder = CustomJSONEncoder

    db.init_app(app)

    return app
