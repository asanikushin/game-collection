from .types import *

from .game import GameProcessor

from service import db


class Storage:
    def __init__(self, game: GameProcessor):
        self.game = game
        self._db = db

    def add_game(self, name, **options) -> ID_WITH_STATUS:
        return self.game.add_game(name, **options)

    def get_game(self, game_id: ID_TYPE) -> GAME_WITH_STATUS:
        return self.get_game(game_id)

    def get_games(self, offset=0, count=None) -> GAMES_WITH_STATUS:
        return self.get_games(offset, count)

    def get_games_count(self) -> int:
        return self.game.get_games_count()

    def delete_game(self, game_id: ID_TYPE) -> GAME_WITH_STATUS:
        return self.game.delete_game(game_id)

    def update_game(self, game_id, method="PATCH", **options) -> GAME_WITH_STATUS:
        return self.game.update_game(game_id, method, **options)
