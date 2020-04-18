import constants
from service.storage import Storage

from utils import create_error

from flask import jsonify, request


def get_user_scores(user_id=None):
    if user_id is None:
        user_id = request.environ["user_id"]
    scores, status = Storage.get_user_scores(user_id=user_id)
    http_status = constants.responses[status]
    return jsonify(scores=scores, status=status), http_status


def get_game_rating(game_id):
    game, status = Storage.get_game_rating(game_id)
    http_status = constants.responses[status]

    if status == constants.statuses["rating"]["returned"]:
        body = dict(rating=game, status=status)
    else:
        body = create_error(status, "no such game id: {{ID}}", ID=game_id)
    return jsonify(body), http_status