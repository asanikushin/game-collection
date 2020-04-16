from .types import *

from utils import check_model_options
from constants import statuses, Methods

from service.models import Game

from service import db
import copy


class GameProcessor:
    def __init__(self):
        self._db = db

    def add_game(self, name, **options) -> ID_WITH_STATUS:
        options.update({"name": name})
        if "id" in options:
            del options["id"]
        correct = check_model_options(Methods.POST, options, Game)
        if correct != statuses["internal"]["correctModelData"]:
            return None, correct

        game = Game(**options)
        self._db.session.add(game)
        self._db.session.commit()
        return game.id, statuses["service"]["created"]

    def get_game(self, game_id) -> GAME_WITH_STATUS:
        if (game := self._get_game(game_id)) is not None:
            return game, statuses["service"]["returned"]
        else:
            return None, statuses["service"]["notExists"]

    def get_games(self, offset=0, count=None) -> GAMES_WITH_STATUS:
        query = self._db.session.query(Game).offset(offset)
        if count is not None:
            query = query.limit(count)
        return query.all(), statuses["service"]["returned"]

    def get_games_count(self) -> int:
        return self._db.session.query(Game).count()

    def delete_game(self, game_id: ID_TYPE) -> GAME_WITH_STATUS:
        if (game := self._get_game(game_id)) is None:
            return None, statuses["service"]["notExists"]
        self._db.session.delete(game)
        return game, statuses["service"]["deleted"]

    def update_game(self, game_id, method="PATCH", **options) -> GAME_WITH_STATUS:
        if (game := self._get_game(game_id)) is None:
            return None, statuses["service"]["notExists"]

        correct = check_model_options(getattr(Methods, method), options, Game, game)
        if correct != statuses["internal"]["correctModelData"]:
            return None, correct
        old = copy.copy(game)
        game.values_update(**options)
        self._db.session.commit()
        return old, statuses["service"]["modified"]

    @staticmethod
    def _get_game(game_id) -> GAME_TYPE:
        return Game.query.get(game_id)
