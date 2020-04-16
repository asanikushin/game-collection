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
        "replacingID": 7,
    },
    "internal": {
        "correctModelData": 8,
    },
    "request": {
        "badArguments": 9,
    },
    "user": {
        "created": 10,
        "emailUsed": 11,
        "wrongPassword": 12,
        "noUser": 13,
        "missingData": 14,
        "invalidEmail": 22,
        "notConfirmed": 23,
        "confirmed": 24,
    },
    "tokens": {
        "created": 15,
        "noSuchToken": 16,
        "refreshTokenExpired": 17,
        "accessTokenExpired": 18,
        "accessOk": 19,
        "missingData": 20,
        "invalidToken": 21,
    }
}


def _check_statuses():
    inverse_status = dict()
    bad = set()
    for key, value in statuses.items():
        for sub_key, status in value.items():
            old = []
            if status in inverse_status:
                bad.add(status)
                old = inverse_status[status]
            inverse_status[status] = old + [(key, sub_key)]

    if len(bad) != 0:
        duplicate = dict()
        for status in bad:
            duplicate[status] = inverse_status[status]
        raise RuntimeError(f"Duplicating status: {bad}: {duplicate}")


_check_statuses()
