from auth.storage import Storage
from utils.pb import auth_pb2
from utils.pb import auth_pb2_grpc
from utils import constants
import grpc

from concurrent import futures
import logging


class AuthServicer(auth_pb2_grpc.AuthServicer):
    def Validate(self, request, context):
        with app.app_context():
            validation, status = Storage.check_token(request.access_token)
        response = auth_pb2.ValidateResponse()
        response.status = status
        if status == constants.statuses["tokens"]["accessOk"]:
            response.user_id = validation["user_id"]
            response.session = validation["session"]
            response.role = validation["role"]
            response.email = validation["email"]
        else:
            response.error = str(validation)
        return response


def create_server(cur_app, port=5001):
    global app
    app = cur_app
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    auth_pb2_grpc.add_AuthServicer_to_server(AuthServicer(), server)
    server.add_insecure_port(f'[::]:{port}')
    logging.info(f"Start gRPC server of port {port}")

    return server
