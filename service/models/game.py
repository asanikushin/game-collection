from service import db
from constants.statuses import statuses


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    category = db.Column(db.String(64), index=True)
    min_players = db.Column(db.Integer, nullable=True)
    max_players = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Game {} - {}: {}>'.format(self.id, self.category, self.name)

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
