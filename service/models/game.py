from service import db


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

    def get_dict(self):
        result = dict(id=self.id, name=self.name, category=self.category)
        result["min_players"] = self.min_players if self.min_players else 0
        result["max_players"] = self.max_players if self.max_players else 0
        return result

    @staticmethod
    def get_fields():
        return ["name", "category"], ["min_players", "max_players"], ["id"]
