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
        correct = check_model_options(Methods.POST, options, Game, service="game")
        if correct != statuses["internal"]["correctModelData"]:
            return None, correct

        game = Game(**options)
        self._db.session.add(game)
        self._db.session.commit()
        return game.id, statuses["game"]["created"]

    def get_game(self, game_id: GAME_ID_TYPE) -> GAME_WITH_STATUS:
        if (game := self._get_game(game_id)) is not None:
            return game, statuses["game"]["returned"]
        else:
            return None, statuses["game"]["notExists"]

    def get_games(self, offset=0, count=None) -> GAMES_WITH_STATUS:
        query = self._db.session.query(Game).offset(offset)
        if count is not None:
            query = query.limit(count)
        return query.all(), statuses["game"]["returned"]

    def get_games_count(self) -> int:
        return self._db.session.query(Game).count()

    def delete_game(self, game_id: GAME_ID_TYPE) -> GAME_WITH_STATUS:
        if (game := self._get_game(game_id)) is None:
            return None, statuses["game"]["notExists"]
        self._db.session.delete(game)
        self._db.session.commit()
        return game, statuses["game"]["deleted"]

    def delete_all_games(self) -> typing.Tuple[int, STATUS]:
        rows_deleted = self._db.session.query(Game).delete()
        self._db.session.commit()
        return rows_deleted, statuses["game"]["deleted"]

    def update_game(self, game_id, method="PATCH", **options) -> GAME_WITH_STATUS:
        if (game := self._get_game(game_id)) is None:
            return None, statuses["game"]["notExists"]

        correct = check_model_options(getattr(Methods, method), options, Game, game, service="game")
        if correct != statuses["internal"]["correctModelData"]:
            return None, correct
        old = copy.copy(game)
        game.values_update(**options)
        self._db.session.commit()
        return old, statuses["game"]["modified"]

    @staticmethod
    def _get_game(game_id) -> GAME_TYPE:
        return Game.query.get(game_id)
