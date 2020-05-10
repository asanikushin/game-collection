from utils import constants, create_error
from service.storage import Storage

from flask import jsonify, request


def get_games():
    options = dict()
    if "offset" in request.args:
        options["offset"] = request.args.get("offset", type=int)
    if "count" in request.args:
        options["count"] = request.args.get("count", type=int)

    if "offset" in options and options["offset"] < 0 or options.get("count", 0) > constants.values.MAX_ELEMENT_COUNT:
        status = constants.statuses["request"]["badArguments"]
        return jsonify(
            create_error(status, "Offset cann't be negative", offset=options["offset"])), constants.responses[status]

    games, status = Storage.get_games(**options)
    http_status = constants.responses[status]
    total_count = Storage.get_games_count()
    count = len(games)
    if len(options) != 0 or count != total_count:
        options["count"] = count
        options["offset"] = options.get("offset", 0)
    return jsonify(games=games, total_count=total_count, status=status, **options), http_status


def get_game(prod_id=None):
    prod_id = prod_id or request.args.get("id")
    game, status = Storage.get_game(prod_id)
    rating, rt_status = Storage.get_game_rating(prod_id)
    http_status = constants.responses[status]

    if status == constants.statuses["game"]["returned"]:
        body = dict(game=game, rating=rating, status=status)
    else:
        body = create_error(status, "no such game id: {{ID}}", ID=prod_id)
    return jsonify(body), http_status
