from loader.storage import Storage
from utils.queues.models import BatchList, BatchElement, Index
from utils.constants import MAX_BATCH_SIZE

from flask import Flask
from lxml import etree

import threading
import os
from typing import Iterable, Callable


def process_message(message: str, app: Flask):
    message = message.split(".")
    app.logger.info(message)
    file_id = message[0]
    if len(message) == 1 or message[1] == "csv":
        threading.Thread(target=process_csv_file, args=(file_id, app,)).start()
    elif message[1] == "xml":
        threading.Thread(target=process_xml_file, args=(file_id, app,)).start()


def process_csv_file(file_id: str, app: Flask):
    def lines_generator():
        for row in file:
            yield row.decode().strip()

    path = os.path.join(app.config["UPLOAD_FOLDER"], file_id)
    with open(path, "rb") as file:
        header = file.readline().decode().strip()
        indexes = Index.parse_from_header(header)
        app.logger.info(f"File {file_id} header {header}")
        app.logger.info(f"File {file_id} indexes {indexes}")

        process_any(file_id, app, lines_generator(), BatchElement.from_csv_row, indexes)


def process_xml_file(file_id: str, app: Flask):
    def tags_generator():
        for event, element in etree.iterparse(file):
            if element.tag != "game":
                continue
            yield element
            element.clear(keep_tail=True)

    path = os.path.join(app.config["UPLOAD_FOLDER"], file_id)
    with open(path, "rb") as file:
        process_any(file_id, app, tags_generator(), BatchElement.from_xml_element)


def process_any(
    file_id: str, app: Flask, iterable: Iterable, converter: Callable, *args, **kwargs
):
    batch = BatchList()
    count = 0
    with app.app_context():
        app.logger.info(f"Process file {file_id}")
        for value in iterable:
            batch.add(converter(value, *args, **kwargs))
            count += 1
            if batch.size() == MAX_BATCH_SIZE:
                app.logger.info(f"process {count} games for {file_id}")
                Storage.add_batch_list(batch, file_id, count)
                batch.clear()

        if batch.size() != 0:
            Storage.add_batch_list(batch, file_id, count)
            app.logger.info(f"process {count} games for {file_id}")
        Storage.add_batch_list(None, file_id, count, True)
        app.logger.info(f"Finish processing file {file_id} with {count} games")
