from utils import constants, create_error
from auth.storage import Storage

from flask import jsonify, request, current_app


def register_user():
    try:
        email = request.json["email"]
        password = request.json["password"]
    except (KeyError, TypeError):
        status = constants.statuses["user"]["missingData"]
        body = create_error(status, "missing user data")
        current_app.logger.warn("Not enough data for sing-up")
        return jsonify(body), constants.responses[status]

    current_app.logger.info(f"Sing up for {email}")

    user_id, status = Storage.add_user(email, password)
    http_status = constants.responses[status]

    if status == constants.statuses["user"]["created"]:
        body = dict(status=status, email=email, user_id=user_id)
    elif status == constants.statuses["user"]["invalidEmail"]:
        body = create_error(status, "email {{email}} is invalid", email=email)
    else:  # status == constants.statuses["user"]["emailUsed"]:
        body = create_error(status, "email {{email}} is already registered", email=email)
    return jsonify(body), http_status
