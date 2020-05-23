from utils import constants, create_error
from service.storage import Storage

from flask import jsonify, request


def get_user_scores(user_id=None):
    if user_id is None:
        user_id = request.environ.get("user_id")
    if user_id is None:
        return (
            jsonify(
                create_error(
                    constants.statuses["user"]["unauthorized"], "No token detected"
                )
            ),
            constants.common_responses["No auth"],
        )
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
