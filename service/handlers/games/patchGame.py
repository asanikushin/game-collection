import constants
from service.storage import Storage

from utils import create_error

from flask import jsonify, request, current_app


def patch_game(prod_id=None):
    prod_id = prod_id or request.args.get("id")
    current_app.logger.info(f"Updating game by {request.environ['user_email']} and game id {prod_id}")

    game, status = Storage.update_game(prod_id, request.method, **request.json)
    http_status = constants.responses[status]

    if status == constants.statuses["game"]["modified"]:
        body = dict(game=game, status=status)
    elif status == constants.statuses["game"]["notExists"]:
        body = create_error(status, "no such game id: {{ID}}", ID=prod_id)
    elif status == constants.statuses["game"]["missingData"]:
        body = create_error(status, "missing game data")
    else:  # status == constants.statuses["game"]["replacingID"]:
        body = create_error(status, "replacing game ID")
    return jsonify(body), http_status
