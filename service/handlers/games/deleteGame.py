from utils import constants, create_error
from service.storage import Storage

from flask import jsonify, request, current_app


def delete_game(prod_id=None):
    prod_id = prod_id or request.args.get("id")
    current_app.logger.info(f"Deleting game by {request.environ['user_email']} and game id {prod_id}")

    game, status = Storage.delete_game(prod_id)
    http_status = constants.responses[status]

    if status == constants.statuses["game"]["deleted"]:
        body = dict(game=game, status=status)
    else:
        body = create_error(status, "no such game id: {{ID}}", ID=prod_id)
    return jsonify(body), http_status


def delete_all_games():
    current_app.logger.info(f"Deleting all games by {request.environ['user_email']}")

    count, status = Storage.delete_all_games()
    http_status = constants.responses[status]

    return jsonify(dict(deleted=count, status=status)), http_status
