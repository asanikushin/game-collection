from utils import constants, create_error
from service.storage import Storage

from flask import jsonify, request, current_app


def delete_score(game_id=None):
    current_app.logger.info(
        f"Deleting score by {request.environ['user_email']} and game id {game_id}"
    )

    game, status = Storage.delete_score(game_id, request.environ["user_id"])
    http_status = constants.responses[status]

    if status == constants.statuses["rating"]["deleted"]:
        body = dict(game=game, status=status)
    else:  # status == constants.statuses["rating"]["notExists"]:
        body = create_error(status, "no your score for game id: {{ID}}", ID=game_id)
    return jsonify(body), http_status
