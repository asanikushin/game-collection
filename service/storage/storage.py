from .types import *

from utils import check_model_options
from constants import statuses

from service.models.game import Game

from service import db


class Storage:
    def __init__(self):
        self._db = db

    def add_game(self, name, **options) -> ID_WITH_STATUS:
        options.update({"name": name})
        if "id" in options:
            del options["id"]
        correct = check_model_options("create", options)
        if correct != statuses["internal"]["correctModelData"]:
            return None, correct

        game = Game(**options)
        self._db.session.add(game)
        self._db.session.commit()
        return game.id, statuses["game"]["created"]

    @staticmethod
    def check_game(game_id) -> bool:
        return Game.query.get(game_id) is not None

    def get_game(self, game_id) -> MODEL_WITH_STATUS:
        game = self._get_game(game_id)
        if game is not None:
            return game, statuses["game"]["returned"]
        else:
            return None, statuses["game"]["notExists"]

    def get_games(self, offset=0, count=None) -> MODELS_WITH_STATUS:
        query = self._db.session.query(Game).offset(offset)
        if count is not None:
            query = query.limit(count)
        return query.all(), statuses["game"]["returned"]

    def get_games_count(self) -> int:
        return self._db.session.query(Game).count()

    def delete_game(self, game_id: ID_TYPE) -> MODEL_WITH_STATUS:
        game = self._get_game(game_id)
        if game is None:
            return None, statuses["game"]["notExists"]
        self._db.session.delete(game)
        return game, statuses["game"]["deleted"]

    def update_game(self, game_id, method="PATCH", **options) -> MODEL_WITH_STATUS:
        game = self._get_game(game_id)
        if game is None:
            return None, statuses["game"]["notExists"]

        correct = check_model_options(method, options, model=game)
        if correct != statuses["internal"]["correctModelData"]:
            return None, correct
        return game.values_update(**options), statuses["game"]["modified"]

    @staticmethod
    def _get_game(game_id) -> MODEL_TYPE:
        return Game.query.get(game_id)
