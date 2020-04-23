from utils import constants
from importer.storage import Storage

from utils.modelq import BatchElement, BatchList

from flask import jsonify, request, current_app
import csv
import uuid

BATCH_SIZE = 1000


def upload_file():
    f = request.files['file']

    file_id = uuid.uuid4()
    current_app.logger.info(f"process file {f.filename} {file_id}")

    batch = BatchList()
    batch_list = []
    header = f.stream.readline().decode().split(',')
    indexes = [1, 3, 7, 5]

    for row in f.stream:
        row = row.decode()
        batch.add(BatchElement.from_row(row, indexes))
        if batch.size() == BATCH_SIZE:
            Storage.add_batch(batch, file_id)
            current_app.logger.info(f"process filed {batch.id} at pos {len(batch_list)}")
            batch_list.append(batch.id)
            batch = BatchList()

    if batch.size() != 0:
        Storage.add_batch(batch, file_id)
        batch_list.append(batch.id)
        current_app.logger.info(f"process filed {batch.id} at pos {len(batch_list)}")

    status = constants.statuses["batch"]["created"]
    return jsonify(file_id=file_id, batch=batch_list, status=status), constants.responses[status]
