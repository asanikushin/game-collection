from importer.storage import Storage
from utils.pb import import_pb2
from utils.pb import import_pb2_grpc
import grpc

from concurrent import futures
import logging


class ImportServicer(import_pb2_grpc.ImportServicer):
    def Load(self, request, context):
        with app.app_context():
            Storage.set_file_status(request.uuid, request.lines, request.loaded)
        response = import_pb2.ImportResponse()
        response.done = True
        return response


def create_server(cur_app, port=5001):
    global app
    app = cur_app
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    import_pb2_grpc.add_ImportServicer_to_server(ImportServicer(), server)
    server.add_insecure_port(f"[::]:{port}")
    logging.info(f"Start gRPC server of port {port}")

    return server
