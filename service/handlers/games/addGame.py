import constants
from service.storage import Storage

from utils import create_error

from flask import jsonify, request, current_app


def add_game():
    current_app.logger.info(f"Creating game by {request.environ['user_email']}")

    new_id, status = Storage.add_game(**request.json)
    http_status = constants.responses[status]

    if status == constants.statuses["game"]["created"]:
        body = dict(id=new_id, status=status)
    else:
        body = create_error(status, "missing game data")
    return jsonify(body), http_status
