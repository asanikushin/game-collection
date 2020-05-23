from utils.constants import statuses
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    category = db.Column(db.String(64), index=True)
    min_players = db.Column(db.Integer, nullable=True)
    max_players = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return "<Game {} - {}: {}>".format(self.id, self.category, self.name)

    def values_update(self, **options):
        self.name = options.get("name", self.name)
        self.category = options.get("category", self.category)
        self.min_players = options.get("min_players", self.min_players)
        self.max_players = options.get("max_players", self.max_players)

    @staticmethod
    def static_check(params):
        min_pl = params.get("min_players")
        max_pl = params.get("max_players")
        if min_pl and min_pl < 0:
            return statuses["game"]["invalidData"]
        if min_pl is not None and max_pl is not None and min_pl > max_pl:
            return statuses["game"]["invalidData"]
        return statuses["internal"]["correctModelData"]

    def data_check(self, params):
        min_pl = params.get("min_players", self.min_players)
        max_pl = params.get("max_players", self.max_players)
        if min_pl and min_pl < 0:
            return statuses["game"]["invalidData"]
        if min_pl is not None and max_pl is not None and min_pl > max_pl:
            return statuses["game"]["invalidData"]
        return statuses["internal"]["correctModelData"]

    def get_dict(self):
        result = dict(id=self.id, name=self.name, category=self.category)
        result["min_players"] = self.min_players if self.min_players else 0
        result["max_players"] = self.max_players if self.max_players else 0
        return result

    @staticmethod
    def get_fields():
        return ["name", "category"], ["min_players", "max_players"], ["id"]


class Rating(db.Model):
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"), primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.FLOAT)

    def __repr__(self):
        return "<Score {} - {}: {}>".format(self.game_id, self.user_id, self.score)

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
