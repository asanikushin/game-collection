from service import db
from constants.statuses import statuses


class Rating(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.FLOAT)

    def __repr__(self):
        return '<Score {} - {}: {}>'.format(self.game_id, self.user_id, self.score)

    def values_update(self, options):
        self.score = options.get("score", self.score)

    def get_dict(self):
        return dict(game_id=self.game_id, user_id=self.user_id, score=self.score)

    @staticmethod
    def static_check(params):
        if (score := params.get("score")) is not None and (score < 0 or score > 10):
            return statuses["rating"]["invalidData"]
        return statuses["internal"]["correctModelData"]

    @staticmethod
    def get_fields():
        return ["game_id", "user_id", "score"], [], ["game_id", "user_id"]
