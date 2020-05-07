from service.storage import Storage
from utils.queues.models import BatchList, BatchElement, Index

from lxml import etree
import threading
import os

BATCH_SIZE = 1000


def process_message(message: str, app):
    message = message.split(".")
    app.logger.info(message)
    file_id = message[0]
    if len(message) == 1 or message[1] == "csv":
        threading.Thread(target=process_csv_file, args=(file_id, app,)).start()
    elif message[1] == "xml":
        threading.Thread(target=process_xml_file, args=(file_id, app,)).start()


def process_csv_file(file_id: str, app):
    path = os.path.join(app.config["UPLOAD_FOLDER"], file_id)
    with open(path) as file:
        with app.app_context():
            header = file.readline().strip()
            app.logger.info(f"File {file_id} header {header}")
            indexes = Index.parse_from_header(header)
            app.logger.info(f"File {file_id} indexes {indexes}")

            batch = BatchList()
            count = 0
            for row in file:
                row = row.strip()
                batch.add(BatchElement.from_csv_row(row, indexes))
                count += 1
                if batch.size() == BATCH_SIZE:
                    app.logger.info(f"process {count} lines for {file_id}")
                    Storage.add_batch_list(batch, file_id, count)
                    batch.clear()

            if batch.size() != 0:
                Storage.add_batch_list(batch, file_id, count)
                app.logger.info(f"process {count} lines for {file_id}")
            Storage.add_batch_list(None, file_id, count, True)
            app.logger.info(f"Finish processing file {file_id} with {count} lines")


def process_xml_file(file_id: str, app):
    path = os.path.join(app.config["UPLOAD_FOLDER"], file_id)
    with open(path, "rb") as file:
        with app.app_context():
            batch = BatchList()
            count = 0
            for event, element in etree.iterparse(file):
                if element.tag != "game":
                    continue

                batch.add(BatchElement.from_xml_element(element))
                count += 1
                if batch.size() == BATCH_SIZE:
                    app.logger.info(f"process {count} games for {file_id}")
                    Storage.add_batch_list(batch, file_id, count)
                    batch.clear()

                element.clear(keep_tail=True)

            if batch.size() != 0:
                Storage.add_batch_list(batch, file_id, count)
                app.logger.info(f"process {count} games for {file_id}")
            Storage.add_batch_list(None, file_id, count, True)
            app.logger.info(f"Finish processing file {file_id} with {count} games")
