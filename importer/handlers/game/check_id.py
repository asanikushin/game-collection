from utils import constants
from importer.storage import Storage

from utils import create_error

from flask import jsonify, request


def check_id():
    batch, file = None, None
    if "batch_id" in request.args:
        batch = request.args.get("batch_id")
    if "file_id" in request.args:
        file = request.args.get("file_id")

    if batch and file:
        status = constants.statuses["request"]["badArguments"]
        return jsonify(create_error(status, "Only one id must be specified")), constants.responses[status]
    if batch is None and file is None:
        status = constants.statuses["request"]["badArguments"]
        return jsonify(create_error(status, "One id must be specified")), constants.responses[status]

    if batch:
        result, status = Storage.batch_status(batch)
        body = dict(batch=result)
    else:  # file
        result, status = Storage.file_status(file)
        body = dict(file=result)

    http_status = constants.responses[status]
    return jsonify(status=status, **body), http_status
