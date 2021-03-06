from typing import Dict

STATUS = int

statuses: Dict[str, Dict[str, STATUS]] = {
    "game": {
        "created": 1,
        "modified": 2,
        "deleted": 3,
        "notExists": 4,
        "returned": 5,
        "missingData": 6,
        "replacingData": 7,
        "extraFields": 34,
        "invalidData": 39,
    },
    "internal": {"correctModelData": 8, "extraModelFields": 25,},
    "request": {"badArguments": 9,},
    "user": {
        "created": 10,
        "emailUsed": 11,
        "wrongPassword": 12,
        "noUser": 13,
        "missingData": 14,
        "invalidEmail": 22,
        "notConfirmed": 23,
        "confirmed": 24,
        "requestNotAllowed": 35,
        "unauthorized": 36,
        "roleChanged": 37,
    },
    "tokens": {
        "created": 15,
        "noSuchToken": 16,
        "refreshTokenExpired": 17,
        "accessTokenExpired": 18,
        "accessOk": 19,
        "missingData": 20,
        "invalidToken": 21,
    },
    "rating": {
        "created": 26,
        "modified": 27,
        "deleted": 28,
        "missingData": 29,
        "replacingData": 30,
        "returned": 31,
        "notExists": 32,
        "extraFields": 33,
        "invalidGameId": 38,
        "invalidData": 40,
    },
    "batch": {"created": 41, "notExists": 42, "returned": 43,},
}
