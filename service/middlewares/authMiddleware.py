from utils.errorResponse import create_error
import constants

from werkzeug.wrappers import Request, Response
import requests
import json


class AuthMiddleware:
    def __init__(self, app, base_app, logger, allowed):
        self.app = app
        self.base = base_app
        self.logger = logger
        self.allowed = allowed

    def __call__(self, environ, start_response):
        request = Request(environ, shallow=True)
        access_token = request.headers.get("accessToken")

        if access_token is None:
            if request.method in ["POST", "DELETE", "PUT", "PATCH"]:  # Modifying requests require accessToken
                self.logger.warn("No token for auth")
                res = Response(json.dumps(create_error(constants.statuses["user"]["unauthorized"],
                                                       "No token detected")),
                               mimetype="application/json",
                               status=constants.common_responses["No auth"])
                return res(environ, start_response)
            return self.app(environ, start_response)

        self.logger.info("Auth request")
        auth_url = self.base.config["AUTH_SERVICE_URI"] + "/validate"
        self.logger.debug(auth_url)

        auth = requests.post(auth_url, json={"token": request.headers["accessToken"]})

        self.logger.debug(str(auth.status_code) + str(auth.content))
        auth_status = auth.json()["status"]

        if auth_status != constants.statuses["tokens"]["accessOk"]:
            auth_error = auth.json()["error"]
            self.logger.warn("Access token is not OK")
            res = Response(json.dumps(create_error(auth_status, auth_error)), mimetype="application/json",
                           status=constants.common_responses["No auth"])
            return res(environ, start_response)
        auth_value = auth.json()["value"]
        environ["user_email"] = auth_value["email"]
        environ["user_id"] = auth_value["user_id"]

        if self._is_allowed(request, environ, auth_value):
            return self.app(environ, start_response)
        else:
            self.logger.warn("User is not allowed to do this request")
            response = json.dumps(create_error(constants.statuses["user"]["requestNotAllowed"],
                                               "You are not allowed to do this request"))
            res = Response(response, mimetype="application/json", status=constants.common_responses["No auth"])
            return res(environ, start_response)

    def _is_allowed(self, request, environ, auth_value):
        if request.method == "GET":
            self.logger.info("Get request with accessToken is always allowed")
            return True
        if auth_value["role"] == constants.UserRole.ADMIN.value:
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
