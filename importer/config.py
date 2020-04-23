import logging
import os

app_dir = os.path.abspath(os.path.dirname(__name__))


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(app_dir, 'importer.db')

    AUTH_SERVICE_SCHEMA = os.environ.get('AUTH_SCHEMA') or 'http://'
    AUTH_SERVICE_URL = os.environ.get('AUTH_URL') or '127.0.0.1'
    AUTH_SERVICE_PORT = os.environ.get('AUTH_PORT') or '5000'
    AUTH_SERVICE_URI = AUTH_SERVICE_URL + ":" + AUTH_SERVICE_PORT

    RABBITMQ = os.environ.get("RABBITMQ")
    QUEUE = os.environ.get("QUEUE")
    LOG_LEVEL = logging.DEBUG


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    LOG_LEVEL = logging.INFO