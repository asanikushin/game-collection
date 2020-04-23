from importer import db
from sqlalchemy_utils import UUIDType


class Batch(db.Model):
    batch_id = db.Column(UUIDType(binary=False), primary_key=True, index=True)
    file_id = db.Column(UUIDType(binary=False), primary_key=True, index=True)
    batch_size = db.Column(db.Integer)
    loaded = db.Column(db.Boolean)

    def __repr__(self):
        return '<Batch {} - {}: {}>'.format(self.file_id, self.batch_id, self.status)

    def values_update(self, **options):
        self.loaded = options.get("status", self.status)

    def get_dict(self):
        result = dict(file=self.file_id, batch=self.batch_id, size=self.batch_size, status=self.loaded)
        return result

    @staticmethod
    def get_fields():
        return ["batch_id", "file_id", "batch_size", "loaded"], [], ["batch_id", "file_id", "batch_size"]
