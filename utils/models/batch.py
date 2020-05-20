from sqlalchemy_utils import UUIDType
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Batch(db.Model):
    file_id = db.Column(UUIDType(binary=False), primary_key=True, index=True)
    loaded = db.Column(db.Boolean)
    lines = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return "<Batch {} - {}: {}>".format(self.file_id, self.lines, self.loaded)

    def values_update(self, options):
        self.loaded = options.get("loaded", self.loaded)
        self.lines = options.get("lines", self.lines)

    def get_dict(self):
        return dict(file=self.file_id, lines=self.lines, status=self.loaded)

    @staticmethod
    def get_fields():
        return ["file_id", "loaded"], ["lines"], ["file_id"]
