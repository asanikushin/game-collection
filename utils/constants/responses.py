from .statuses import STATUS, statuses
from typing import Dict
import logging as __log

RESPONSE = int
responses: Dict[STATUS, RESPONSE] = {
    statuses["game"]["created"]: 201,
    statuses["game"]["modified"]: 202,
    statuses["game"]["deleted"]: 200,
    statuses["game"]["notExists"]: 404,
    statuses["game"]["returned"]: 200,
    statuses["game"]["missingData"]: 400,
    statuses["game"]["replacingData"]: 403,
    statuses["game"]["extraFields"]: 400,
    statuses["game"]["invalidData"]: 400,

    statuses["request"]["badArguments"]: 400,

    statuses["user"]["created"]: 201,
    statuses["user"]["emailUsed"]: 406,
    statuses["user"]["wrongPassword"]: 403,
    statuses["user"]["noUser"]: 404,
    statuses["user"]["missingData"]: 400,
    statuses["user"]["invalidEmail"]: 400,
    statuses["user"]["notConfirmed"]: 400,
    statuses["user"]["confirmed"]: 200,
    statuses["user"]["requestNotAllowed"]: 403,
    statuses["user"]["unauthorized"]: 401,
    statuses["user"]["roleChanged"]: 200,

    statuses["tokens"]["created"]: 201,
    statuses["tokens"]["noSuchToken"]: 404,
    statuses["tokens"]["refreshTokenExpired"]: 403,
    statuses["tokens"]["accessTokenExpired"]: 403,
    statuses["tokens"]["accessOk"]: 200,
    statuses["tokens"]["missingData"]: 400,
    statuses["tokens"]["invalidToken"]: 406,

    statuses["rating"]["created"]: 201,
    statuses["rating"]["modified"]: 202,
    statuses["rating"]["deleted"]: 200,
    statuses["rating"]["missingData"]: 400,
    statuses["rating"]["replacingData"]: 403,
    statuses["rating"]["returned"]: 200,
    statuses["rating"]["notExists"]: 404,
    statuses["rating"]["extraFields"]: 400,
    statuses["rating"]["invalidGameId"]: 400,
    statuses["rating"]["invalidData"]: 400,

    statuses["batch"]["created"]: 201,
    statuses["batch"]["notExists"]: 404,
    statuses["batch"]["returned"]: 200,
}

common_responses: Dict[str, RESPONSE] = {
    "Bad request": 400,
    "No auth": 401,
    "Not found": 404,
}
