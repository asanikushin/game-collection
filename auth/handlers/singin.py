from utils import constants, create_error
from auth.storage import Storage

from flask import jsonify, request, current_app


def sign_in():
    try:
        email = request.json["email"]
        password = request.json["password"]
    except KeyError:
        status = constants.statuses["user"]["missingData"]
        body = create_error(status, "missing user data")
        current_app.logger.warn("Not enough data for sing-in")
        return jsonify(body), constants.responses[status]

    current_app.logger.info(f"Sing in for {email}")

    access, refresh, status = Storage.create_session(email, password)
    http_status = constants.responses[status]

    if status == constants.statuses["tokens"]["created"]:
        body = dict(status=status, accessToken=access, refreshToken=refresh)
    elif status == constants.statuses["user"]["wrongPassword"]:
        body = create_error(status, "wrong password for email {{email}}", email=email)
    elif status == constants.statuses["user"]["notConfirmed"]:
        body = create_error(status, "Account not confirmed")
    else:  # status == constants.statuses["user"]["noUser"]:
        body = create_error(status, "No user for email {{email}}", email=email)
    return jsonify(body), http_status
