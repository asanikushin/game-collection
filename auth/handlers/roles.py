from utils import constants, create_error
from auth.storage import Storage

from flask import jsonify, request, current_app


def change_role():
    current_app.logger.info("Make other user admin")
    if (token := request.headers.get("Authorization")) is None:
        status = constants.statuses["user"]["unauthorized"]
        body = create_error(status, "No token get")
        current_app.logger.warn("No token detected")
        return jsonify(body), constants.responses[status]
    token = token.strip("Bearer ")

    if (user_id := request.json.get("user_id")) is None or (role := request.json.get("role")) is None:
        status = constants.statuses["user"]["missingData"]
        return jsonify(create_error(status, "Not enough data to change role")), constants.responses[status]

    status = Storage.change_role(token, user_id, role)
    http_status = constants.responses[status]

    if status == constants.statuses["user"]["roleChanged"]:
        body = dict(status=status)
    elif status == constants.statuses["tokens"]["invalidToken"]:
        body = create_error(status, "Invalid admin access token")
    else:  # status == constants.statuses["user"]["requestNotAllowed"]:
        body = create_error(status, "User is not allowed to do this request")

    return jsonify(body), http_status
