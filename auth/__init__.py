from utils import CustomJSONEncoder

import auth.config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import logging
import os

db = SQLAlchemy()
migrate = Migrate()

logging.basicConfig(
    format='%(asctime)s %(name)-8s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def create_app(config_class="auth.config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(os.environ.get('FLASK_ENV') or config_class)
    app.json_encoder = CustomJSONEncoder

    db.init_app(app)
    migrate.init_app(app, db)

    from auth.handlers import auth

    app.register_blueprint(auth, url_prefix="/")

    log = logging.getLogger(app.name)
    log.setLevel(app.config["LOG_LEVEL"])

    return app
