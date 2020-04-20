from .types import *

from service.models import Rating

from service import db

from utils import check_model_options
from utils.constants import statuses, Methods

from sqlalchemy import func


class RatingProcessor:
    def __init__(self):
        self._db = db

    def add_score(self, parameters) -> RAT_WITH_STATUS:
        correct = check_model_options(Methods.POST, parameters, Rating, service="rating")
        if correct != statuses["internal"]["correctModelData"]:
            return None, correct
        if (previous := self._get_score(parameters["game_id"], parameters["user_id"])) is not None:
            return self.update_score(parameters, "UPDATE")
        score = Rating(game_id=parameters["game_id"], user_id=parameters["user_id"], score=parameters["score"])
        self._db.session.add(score)
        self._db.session.commit()
        return score, statuses["rating"]["created"]

    def delete_user_score(self, game_id: GAME_ID_TYPE, user_id) -> RAT_WITH_STATUS:
        if (score := self._get_score(game_id, user_id)) is None:
            return None, statuses["rating"]["notExists"]
        self._db.session.delete(score)
        self._db.session.commit()
        return score, statuses["rating"]["deleted"]

    def delete_game_score(self, game_id: GAME_ID_TYPE) -> typing.Tuple[int, STATUS]:
        rows_deleted = self._db.session.query(Rating).filter(Rating.game_id == game_id).delete()
        self._db.session.commit()
        return rows_deleted, statuses["rating"]["deleted"]

    def delete_all_scores(self):
        rows_deleted = self._db.session.query(Rating).delete()
        self._db.session.commit()
        return rows_deleted, statuses["rating"]["deleted"]

    @staticmethod
    def get_game_rating(game_id: GAME_ID_TYPE) -> RATING_WITH_STATUS:
        val = Rating.query.with_entities(func.avg(Rating.score)).filter(Rating.game_id == game_id) \
            .group_by(Rating.game_id).first()
        val = val[0] if val else 0
        return val, statuses["rating"]["returned"]

    @staticmethod
    def get_user_scores(user_id) -> RAT_WITH_STATUS:
        return Rating.query.filter(Rating.user_id == user_id).all(), statuses["rating"]["returned"]

    def update_score(self, parameters, method) -> RAT_WITH_STATUS:
        game_id = parameters["game_id"]
        user_id = parameters["user_id"]
        if (score := self._get_score(game_id, user_id)) is None:
            return None, statuses["rating"]["notExists"]

        correct = check_model_options(getattr(Methods, method), parameters, Rating, score, service="rating")
        if correct != statuses["internal"]["correctModelData"]:
            return None, correct
        score.values_update(parameters)
        self._db.session.commit()
        return score, statuses["rating"]["modified"]

    @staticmethod
    def _get_score(game_id: GAME_ID_TYPE, user_id) -> Rating:
        return Rating.query.get((game_id, user_id))
