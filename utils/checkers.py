from constants import STATUS, statuses
from typing import Dict, Optional

from validate_email import validate_email


def check_keys(base: Dict, *keys, all=False) -> bool:
    for key in keys:
        if key not in base and all:  # all keys in base
            return False
        if key in base and not all:  # any of keys in base
            return True
    return all


def check_model_options(operation: str, options: Dict, model=None) -> STATUS:
    if operation == "create":
        if check_keys(options, "name", "category"):
            return statuses["internal"]["correctModelData"]
        else:
            return statuses["product"]["missingData"]
    elif operation.lower() in ["patch"]:
        opt_id = options.get("id", None)
        if opt_id is None or model is None:
            correct_id = True
        else:
            correct_id = (opt_id == model.id)

        if not correct_id:
            return statuses["product"]["replacingID"]
        if check_keys(options, "name", "category", all=False):
            return statuses["internal"]["correctModelData"]
        else:
            return statuses["product"]["missingData"]
    else:
        raise NotImplemented()


def check_email(email: str) -> Optional[str]:
    if validate_email(email):
        return email
    return None
