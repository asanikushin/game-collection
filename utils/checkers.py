from constants import STATUS, statuses, Methods
from typing import Dict, Optional, Union

from validate_email import validate_email


def check_keys(base: Dict, *keys, all=False) -> bool:
    for key in keys:
        if key not in base and all:  # all keys in base
            return False
        if key in base and not all:  # any of keys in base
            return True
    return all


# TODO add check for other fields
def check_model_options(operation: Methods, options: Dict, cls, instance=object, service="service") -> STATUS:
    must, other, constr = cls.get_fields()
    all_fields = set(must + other)

    if len(set(options.keys()).difference(all_fields)) != 0:
        return statuses[service]["extraFields"]

    if operation == Methods.POST:
        if check_keys(options, *must):
            return statuses["internal"]["correctModelData"]
        else:
            return statuses[service]["missingData"]
    elif operation == Methods.PUT or operation == Methods.PATCH:
        if instance:
            for field in constr:
                if (val := options.get(field, None)) is not None and val != getattr(instance, field):
                    return statuses[service]["replacingData"]
        return statuses["internal"]["correctModelData"]
    else:
        raise NotImplementedError()


def check_email(email: str) -> Optional[str]:
    if validate_email(email):
        return email
    return None
