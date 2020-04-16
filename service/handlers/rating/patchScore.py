import constants
from service.storage import Storage

from utils import create_error

from flask import jsonify, request, current_app


def patch_score(game_id):
    # TODO try for data from request
    current_app.logger.info(f"Updating score by {request.environ['user_email']} and game id {game_id}")

    request.json["user_id"] = request.environ["user_id"]
    request.json["game_id"] = game_id

    score, status = Storage.update_score(request.json, request.method)
    http_status = constants.responses[status]

    if status == constants.statuses["rating"]["modified"]:
        body = dict(score=score, status=status)
    elif status == constants.statuses["rating"]["notExists"]:
        body = create_error(status, "no such score")
    elif status == constants.statuses["rating"]["missingData"]:
        body = create_error(status, "missing score data")
    else:  # status == constants.statuses["rating"]["replacingData"]:
        body = create_error(status, "replacing score IDs")
    return jsonify(body), http_status
