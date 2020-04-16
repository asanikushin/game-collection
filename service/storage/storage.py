from .types import *

from .game import GameProcessor
from .rating import RatingProcessor

from service import db


class Storage:
    def __init__(self, game: GameProcessor, rating: RatingProcessor):
        self.game = game
        self.rating = rating
        self._db = db

    # Game handlers
    def add_game(self, name, **options) -> ID_WITH_STATUS:
        return self.game.add_game(name, **options)

    def get_game(self, game_id: GAME_ID_TYPE) -> GAME_WITH_STATUS:
        return self.game.get_game(game_id)

    def get_games(self, offset=0, count=None) -> GAMES_WITH_STATUS:
        return self.game.get_games(offset, count)

    def get_games_count(self) -> int:
        return self.game.get_games_count()

    def delete_game(self, game_id: GAME_ID_TYPE) -> GAME_WITH_STATUS:
        return self.game.delete_game(game_id)

    def update_game(self, game_id, method="PATCH", **options) -> GAME_WITH_STATUS:
        return self.game.update_game(game_id, method, **options)

    # Rating handlers
    def add_score(self, params) -> RAT_WITH_STATUS:
        return self.rating.add_score(params)

    def delete_score(self, game_id: GAME_ID_TYPE, user_id) -> RAT_WITH_STATUS:
        return self.rating.delete_score(game_id, user_id)

    def get_game_rating(self, game_id: GAME_ID_TYPE) -> RATING_WITH_STATUS:
        return self.rating.get_game_rating(game_id)

    def get_user_scores(self, user_id) -> RAT_WITH_STATUS:
        return self.rating.get_user_scores(user_id)

    def update_score(self, params, method) -> RAT_WITH_STATUS:
        return self.rating.update_score(params, method)
