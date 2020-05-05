from utils import constants, create_error
from service.storage import Storage

from flask import jsonify, request, current_app


def add_score():
    current_app.logger.info(f"Add score to game {request.json.get('game_id')} by {request.environ['user_email']}")

    request.json["user_id"] = request.environ["user_id"]
    score, status = Storage.add_score(request.json)
    http_status = constants.responses[status]

    if status == constants.statuses["rating"]["created"]:
        body = dict(score=score, status=status)
    elif status == constants.statuses["rating"]["missingData"]:
        body = create_error(status, "missing score data")
    elif status == constants.statuses["rating"]["extraFields"]:
        body = create_error(status, "Extra fields in data")
    elif status == constants.statuses["rating"]["invalidData"]:
        body = create_error(status, "Rating data is invalid")
    else:  # status == constants.statuses["rating"]["invalidGameId"]:
        body = create_error(status, "No game with such {{id}}", id=request.json.get('game_id'))
    return jsonify(body), http_status
