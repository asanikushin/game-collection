from enum import Enum


class Methods(Enum):
    POST = "POST"
    GET = "GET"
    DELETE = "DELETE"
    PUT = "PUT"
    PATCH = "PATCH"


class UserRole(Enum):
    ADMIN = "ADMIN"
    BASE = "BASE"
    DEFAULT = BASE
