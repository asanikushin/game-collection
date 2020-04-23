from .types import *

from importer import db
from importer.models import Batch

from utils.constants import statuses

from utils.queues import wait_connection, send_message
from utils.modelq import BatchList, BatchElement

from flask import current_app
import pickle


class Storage:
    def __init__(self):
        self._db = db
        self._rabbit = None

    def _init_rabbit_connection(self):
        self._rabbit = wait_connection(current_app.config["RABBITMQ"], current_app.logger)

    def add_batch(self, data: BatchList, file_id):
        batch = Batch(file_id=file_id)
        batch.batch_id = data.id
        batch.loaded = False
        batch.batch_size = data.size()

        self._db.session.add(batch)
        self._db.session.commit()
        self.send_batch(data)

    def send_batch(self, data: BatchList):
        if self._rabbit is None:
            self._init_rabbit_connection()
        send_message(self._rabbit, current_app.config["QUEUE"], pickle.dumps(data))
        self._rabbit = None

    def batch_status(self, batch_id):
        if (batch := self._get_batch(batch_id)) is None:
            return None, statuses["batch"]["notExists"]
        return batch, statuses["batch"]["returned"]

    @staticmethod
    def file_status(file_id):
        return Batch.query.filter(Batch.file_id == file_id).all(), statuses["batch"]["returned"]

    def set_batch_status(self, batch_id, loaded: bool):
        if (batch := self._get_batch(batch_id)) is None:
            return
        batch.loaded = loaded
        self._db.session.commit()

    @staticmethod
    def _get_batch(batch_id):
        return Batch.query.filter(Batch.batch_id == batch_id).first()
