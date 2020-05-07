from .types import *

from utils import check_model_options
from utils.constants import statuses, Methods, MAX_ELEMENT_COUNT
from utils.queues.models import BatchList

from service.models import Game

from service import db


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

    @staticmethod
    def get_game(game_id: GAME_ID_TYPE) -> GAME_WITH_STATUS:
        if (game := GameProcessor._get_game(game_id)) is not None:
            return game, statuses["game"]["returned"]
        else:
            return None, statuses["game"]["notExists"]

    def get_games(self, offset=0, count=None) -> GAMES_WITH_STATUS:
        query = self._db.session.query(Game).offset(offset)
        if count is None or count > MAX_ELEMENT_COUNT:
            count = MAX_ELEMENT_COUNT
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

    def delete_all_games(self) -> COUNT_WITH_STATUS:
        rows_deleted = self._db.session.query(Game).delete()
        self._db.session.commit()
        return rows_deleted, statuses["game"]["deleted"]

    def update_game(self, game_id, method="PATCH", **options) -> GAME_WITH_STATUS:
        if (game := self._get_game(game_id)) is None:
            return None, statuses["game"]["notExists"]

        correct = check_model_options(getattr(Methods, method), options, Game, game, service="game")
        if correct != statuses["internal"]["correctModelData"]:
            return None, correct
        game.values_update(**options)
        self._db.session.commit()
        return game, statuses["game"]["modified"]

    def add_batch_list(self, batch: BatchList) -> None:
        for element in batch.to_list():
            game = Game(**element.get_dict())
            self._db.session.add(game)
        self._db.session.commit()

    @staticmethod
    def _get_game(game_id) -> GAME_TYPE:
        return Game.query.get(game_id)
