from utils import constants, create_error
from auth.storage import Storage

from flask import jsonify, current_app


def confirm(token: str):
    current_app.logger.info(f"Confirming user")
    current_app.logger.debug(f"Confirm by token {token}")

    body, status = Storage.confirm_user(token)
    http_status = constants.responses[status]

    if status == constants.statuses["user"]["confirmed"]:
        body = dict(status=status, body=body)
    elif status == constants.statuses["tokens"]["invalidToken"]:
        body = create_error(status, "Access token has invalid format", error=body)
    return jsonify(body), http_status
