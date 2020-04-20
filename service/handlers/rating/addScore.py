import constants
from service.storage import Storage

from utils import create_error

from flask import jsonify, request, current_app


def add_score():
    # TODO try for data from request
    current_app.logger.info(f"Add score to game {request.json.get('game_id')} by {request.environ['user_email']}")

    request.json["user_id"] = request.environ["user_id"]
    score, status = Storage.add_score(request.json)
    http_status = constants.responses[status]

    if status == constants.statuses["rating"]["created"]:
        body = dict(score=score, status=status)
    elif status == constants.statuses["rating"]["missingData"]:
        body = create_error(status, "missing score data")
    else:  # status == constants.statuses["rating"]["invalidGameId"]:
        body = create_error(status, "No game with such {{id}}", id=request.json.get('game_id'))
    return jsonify(body), http_status
