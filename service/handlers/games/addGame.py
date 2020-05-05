from utils import constants, create_error
from service.storage import Storage

from flask import jsonify, request, current_app


def add_game():
    current_app.logger.info(f"Creating game by {request.environ['user_email']}")

    new_id, status = Storage.add_game(**request.json)
    http_status = constants.responses[status]

    if status == constants.statuses["game"]["created"]:
        body = dict(id=new_id, status=status)
    elif status == constants.statuses["game"]["missingData"]:
        body = create_error(status, "missing game data")
    elif status == constants.statuses["game"]["extraFields"]:
        body = create_error(status, "Extra fields in data")
    else:  # status == constants.statuses["game"]["invalidData"]:
        body = create_error(status, "Game data is invalid")
    return jsonify(body), http_status
