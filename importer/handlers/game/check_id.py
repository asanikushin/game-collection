from utils import constants, create_error
from importer.storage import Storage

from flask import jsonify, request


def check_id():
    file_id = request.args.get("file_id")
    if file_id is None:
        status = constants.statuses["request"]["badArguments"]
        return (
            jsonify(create_error(status, "One id must be specified")),
            constants.responses[status],
        )

    result, status = Storage.file_status(file_id)
    http_status = constants.responses[status]

    if status == constants.statuses["batch"]["returned"]:
        body = dict(status=status, file=result)
    else:
        body = create_error(status, "no such file id: {{ID}}", ID=file_id)

    return jsonify(body), http_status
