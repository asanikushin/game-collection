from .types import *

from importer import db
from utils.models.batch import Batch

from utils.constants import statuses
from utils.queues import wait_connection, send_message

from flask import current_app


class Storage:
    def __init__(self):
        self._db = db
        self._rabbit = None

    def _init_rabbit_connection(self):
        self._rabbit = wait_connection(
            current_app.config["RABBITMQ"], current_app.logger
        )

    def add_file(self, file_id: FILE_ID_TYPE, extension="") -> STATUS:
        file = self._add_file(file_id)
        file.loaded = False
        file.lines = 0

        self._db.session.commit()

        self.send_file(str(file_id) + extension)
        return statuses["batch"]["created"]

    @staticmethod
    def file_status(file_id: FILE_ID_TYPE) -> ID_WITH_STATUS:
        if (file := Storage._get_file(file_id)) is not None:
            return file, statuses["batch"]["returned"]
        else:
            return None, statuses["batch"]["notExists"]

    def set_file_status(self, file_id: FILE_ID_TYPE, lines: int, loaded: bool):
        if (file := self._get_file(file_id)) is None:
            file = self._add_file(file_id)
        file.loaded = loaded or file.loaded
        file.lines = max(lines or 0, file.lines or 0)
        self._db.session.commit()

    def send_file(self, file_id: FILE_TYPE):
        if self._rabbit is None:
            self._init_rabbit_connection()
        send_message(self._rabbit, current_app.config["QUEUE"], str(file_id))
        self._rabbit = None

    def _add_file(self, file_id: FILE_ID_TYPE) -> Batch:
        file = Batch(file_id=file_id)
        self._db.session.add(file)
        return file

    @staticmethod
    def _get_file(file_id: FILE_ID_TYPE):
        return Batch.query.get(file_id)
