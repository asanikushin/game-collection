from utils import constants
from importer.storage import Storage

from flask import jsonify, request, current_app
import uuid

import os


def upload_file():
    values = {}
    for file in request.files:
        f = request.files[file]

        filename, file_extension = os.path.splitext(f.filename)

        file_id = str(uuid.uuid4())
        current_app.logger.info(f"process file {f.filename} as {file_id}{file_extension}")
        f.save(os.path.join(current_app.config["UPLOAD_FOLDER"], str(file_id)))

        Storage.add_file(file_id, file_extension)
        values[file] = file_id
    status = constants.statuses["batch"]["created"]
    return jsonify(files=values, status=status), constants.responses[status]
