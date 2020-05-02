from utils import constants
from importer.storage import Storage

from utils.queues.models import BatchElement, BatchList

from flask import jsonify, request, current_app
import uuid

BATCH_SIZE = 1000


def upload_file():
    f = request.files['file']

    file_id = uuid.uuid4()
    current_app.logger.info(f"process file {f.filename} {file_id}")

    header = f.stream.readline().decode().strip().split(',')
    current_app.logger.info(f"File header {header}")
    indexes = [
        header.index("name"),
        header.index("categories"),
        header.index("min_players"),
        header.index("max_players"),
    ]
    current_app.logger.info(f"File indexes {indexes}")

    batch = BatchList()
    batch_list = []
    for row in f.stream:
        row = row.decode().strip()
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
