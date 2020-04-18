from utils import CustomJSONEncoder

import service.config

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


def create_app(config_class="service.config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(os.environ.get('FLASK_ENV') or config_class)
    app.json_encoder = CustomJSONEncoder

    db.init_app(app)
    migrate.init_app(app, db)

    from service.handlers import games, rating

    app.register_blueprint(games, url_prefix="/games")
    app.register_blueprint(rating, url_prefix="/rating")

    from service.middlewares.loggerMiddleware import LoggerMiddleware
    from service.middlewares.authMiddleware import AuthMiddleware

    log = logging.getLogger(app.name)
    log.setLevel(app.config["LOG_LEVEL"])

    app.wsgi_app = AuthMiddleware(app.wsgi_app, app, log, (
        ("/rating", "POST"),
        ("/rating", "PUT"),
        ("/rating", "PATCH"),
        ("/rating", "DELETE"),
    ))

    app.wsgi_app = LoggerMiddleware(app.wsgi_app, log)

    return app
