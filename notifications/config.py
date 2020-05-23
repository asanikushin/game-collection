import logging
import os


class BaseConfig:
    SMTP_URL = os.environ.get("SMTP_URL") or "127.0.0.1"
    SMTP_PORT = os.environ.get("SMTP_PORT") or "25"
    SMTP_URI = SMTP_URL + ":" + SMTP_PORT

    FROM_EMAIL = os.environ.get("FROM_EMAIL") or "test@email"

    RABBITMQ = os.environ.get("RABBITMQ") or "rabbitmq"
    QUEUE = os.environ.get("QUEUE") or "notifications"

    LOG_LEVEL = logging.DEBUG
