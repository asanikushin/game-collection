from loader import db

from utils.models.games import Game
from utils.queues import BatchList
from utils.pb.import_pb2 import ImportRequest
from utils.pb.import_pb2_grpc import ImportStub

from flask import current_app
import grpc
from typing import Optional


class _Storage:
    def __init__(self):
        self._db = db

        self.rpc_connection = None
        self.load_stub: Optional[ImportStub] = None

    def _init_rpc(self):
        self.rpc_connection = grpc.insecure_channel(current_app.config["IMPORTER_GRPC"])
        self.load_stub: ImportStub = ImportStub(self.rpc_connection)

    def add_batch_list(self, batch: Optional[BatchList], file_id, lines, loaded=False):
        if batch is not None:
            for element in batch.to_list():
                game = Game(**element.get_dict())
                self._db.session.add(game)
            self._db.session.commit()

        request = ImportRequest(uuid=str(file_id), lines=lines, loaded=loaded)
        if self.load_stub is None:
            self._init_rpc()
        self.load_stub.Load(request)


Storage = _Storage()
