from service import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    category = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<Game {} - {}: {}>'.format(self.id, self.category, self.name)

    def values_update(self, **options):
        self.name = options.get("name", self.name)
        self.category = options.get("category", self.category)

    def get_dict(self):
        return dict(id=self.id, name=self.name, category=self.category)
