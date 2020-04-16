from .addGame import add_game
from .deleteGame import delete_game
from .getGame import get_game, get_games
from .patchGame import patch_game

from flask import Blueprint

games = Blueprint("games", __name__)

games.add_url_rule("/", "add_games", add_game, methods=['POST'])

games.add_url_rule("/<int:prod_id>", "delete_game", delete_game, methods=['DELETE'])

games.add_url_rule("/", "get_games", get_games, methods=["GET"])
games.add_url_rule("/<int:prod_id>", "get_game", get_game, methods=["GET"])

games.add_url_rule("/<int:prod_id>", "patch_game", patch_game, methods=['PATCH', 'PUT'])

