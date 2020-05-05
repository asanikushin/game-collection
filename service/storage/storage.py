from .types import *
from .game import GameProcessor
from .rating import RatingProcessor

from service import db

from utils.constants import statuses
from utils.modelq import BatchList
from utils.pb.import_pb2 import ImportRequest
from utils.pb.import_pb2_grpc import ImportStub

from flask import current_app
import grpc


class Storage:
    def __init__(self, game: GameProcessor, rating: RatingProcessor):
        self.game = game
        self.rating = rating
        self._db = db

        self.rpc_connection = None
        self.load_stub = None

    def _init_rpc(self):
        self.rpc_connection = grpc.insecure_channel(current_app.config["IMPORTER_GRPC"])
        self.load_stub = ImportStub(self.rpc_connection)

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
        result = self.game.delete_game(game_id)
        self.rating.delete_game_score(game_id)
        return result

    def delete_all_games(self) -> typing.Tuple[int, STATUS]:
        result = self.game.delete_all_games()
        self.rating.delete_all_scores()
        return result

    def update_game(self, game_id, method="PATCH", **options) -> GAME_WITH_STATUS:
        return self.game.update_game(game_id, method, **options)

    def add_batch_list(self, batch: BatchList, file_id, lines, loaded=False):
        if batch is not None:
            self.game.add_batch_list(batch)

        request = ImportRequest(uuid=str(file_id), lines=lines, loaded=loaded)
        if self.load_stub is None:
            self._init_rpc()
        self.load_stub.Load(request)

    # Rating handlers
    def add_score(self, params) -> RAT_WITH_STATUS:
        game, status = self.get_game(params.get("game_id"))
        if status != statuses["game"]["returned"]:
            return None, statuses["rating"]["invalidGameId"]
        return self.rating.add_score(params)

    def delete_score(self, game_id: GAME_ID_TYPE, user_id) -> RAT_WITH_STATUS:
        return self.rating.delete_user_score(game_id, user_id)

    def get_game_rating(self, game_id: GAME_ID_TYPE) -> RATING_WITH_STATUS:
        return self.rating.get_game_rating(game_id)

    def get_user_scores(self, user_id) -> RAT_WITH_STATUS:
        return self.rating.get_user_scores(user_id)

    def update_score(self, params, method) -> RAT_WITH_STATUS:
        return self.rating.update_score(params, method)
