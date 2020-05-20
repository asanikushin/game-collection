import logging
import os

app_dir = os.path.abspath(os.path.dirname(__name__))


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI"
    ) or "sqlite:///" + os.path.join(app_dir, "service.db")

    AUTH_GRPC = os.environ.get("AUTH_GRPC") or "localhost:5001"

    LOG_LEVEL = logging.DEBUG


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    LOG_LEVEL = logging.INFO
