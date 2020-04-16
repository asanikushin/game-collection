from service import db


class Rating(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)

    def __repr__(self):
        return '<Score {} - {}: {}>'.format(self.game_id, self.user_id, self.score)

    def values_update(self, options):
        self.score = options.get("score", self.score)

    def get_dict(self):
        return dict(game_id=self.game_id, user_id=self.user_id, score=self.score)

    @staticmethod
    def get_fields():
        return ["game_id", "user_id", "score"], [], ["game_id", "user_id"]
