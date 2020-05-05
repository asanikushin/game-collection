from utils import constants
from importer.storage import Storage

from flask import jsonify, request, current_app
import uuid

import os


def upload_file():
    f = request.files['file']

    file_id = uuid.uuid4()
    current_app.logger.info(f"process file {f.filename} {file_id}")
    f.save(os.path.join(current_app.config["UPLOAD_FOLDER"], str(file_id)))

    status = Storage.add_file(file_id)

    return jsonify(file_id=file_id, status=status), constants.responses[status]
