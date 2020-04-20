from utils.errorResponse import create_error
import constants

from pb.auth_pb2 import ValidateRequest
from pb.auth_pb2_grpc import AuthStub

from werkzeug.wrappers import Request, Response
import grpc
import json


class AuthMiddleware:
    def __init__(self, app, base_app, logger, allowed):
        self.app = app
        self.base = base_app
        self.logger = logger
        self.allowed = allowed

        self.auth_method = "Bearer "

        self.rpc_connection = grpc.insecure_channel(self.base.config["AUTH_SERVICE_URI"])
        self.validate_stub = AuthStub(self.rpc_connection)


    def __call__(self, environ, start_response):
        request = Request(environ, shallow=True)

        if (authorization := request.headers.get("Authorization")) is None:
            if request.method in ["POST", "DELETE", "PUT", "PATCH"]:  # Modifying requests require accessToken
                self.logger.warn("No token for auth")
                res = Response(json.dumps(create_error(constants.statuses["user"]["unauthorized"],
                                                       "No token detected")),
                               mimetype="application/json",
                               status=constants.common_responses["No auth"])
                return res(environ, start_response)
            return self.app(environ, start_response)
        elif type(authorization) != str or not authorization.startswith(self.auth_method):
            self.logger.warn("Invalid Authorization method")
            res = Response(json.dumps(create_error(constants.statuses["user"]["unauthorized"],
                                                   "Invalid Authorization method")),
                           mimetype="application/json",
                           status=constants.common_responses["No auth"])
            return res(environ, start_response)

        self.logger.info("Auth request")
        
        access_token = authorization[len(self.auth_method):]
        validate_request = ValidateRequest(access_token=access_token)
        auth = self.validate_stub.Validate(validate_request)

        if auth.status != constants.statuses["tokens"]["accessOk"]:
            self.logger.warn("Access token is not OK")
            res = Response(json.dumps(create_error(auth.status, auth.error)), mimetype="application/json",
                           status=constants.common_responses["No auth"])
            return res(environ, start_response)

        environ["user_email"] = auth.email
        environ["user_id"] = auth.user_id

        if self._is_allowed(request, environ, auth):
            return self.app(environ, start_response)
        else:
            self.logger.warn("User is not allowed to do this request")
            response = json.dumps(create_error(constants.statuses["user"]["requestNotAllowed"],
                                               "You are not allowed to do this request"))
            res = Response(response, mimetype="application/json", status=constants.common_responses["No auth"])
            return res(environ, start_response)

    def _is_allowed(self, request, environ, auth):
        if request.method == "GET":
            self.logger.info("Get request with accessToken is always allowed")
            return True
        if auth.role == constants.UserRole.ADMIN.value:
            self.logger.info("Request for admin user is always allowed")
            return True
        path = request.path
        method = request.method
        for route in self.allowed:
            if method != route[1]:
                continue
            if path[:len(route[0])] == route[0]:
                return True
        return False
