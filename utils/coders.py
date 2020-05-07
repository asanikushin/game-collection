from utils.constants import STATUS

import datetime
import decimal
from json import JSONEncoder
from typing import Any, Dict, List, Optional
import uuid


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        try:
            return o.get_dict()
        except AttributeError:
            pass
        if isinstance(o, (decimal.Decimal, uuid.UUID)):
            return str(o)
        return o.__dict__


def parse_csv_row(row: str) -> List[str]:
    result = []
    cur = ""
    is_str = False
    for token in row:
        if token == "," and not is_str:
            result.append(cur)
            cur = ""
        elif token == "\"":
            is_str = not is_str
        else:
            cur += token
    if len(result) != 0 or len(cur) != 0:
        result.append(cur)
    return result


def my_int(val: Optional[str]) -> int:
    if val is None or val == "":
        return 0
    return int(val)


def parse_timedelta(delta: Optional[str]) -> Optional[datetime.timedelta]:
    if delta is None:
        return None
    options = dict()
    for token in delta.split():
        unit = token[-1].upper()
        value = int(token[:-1])
        if unit == "S":
            options["seconds"] = value
        elif unit == "M":
            options["minutes"] = value
        elif unit == "H":
            options["hours"] = value
        elif unit == "W":
            options["weeks"] = value
        else:
            raise ValueError("No such delta period")
    return datetime.timedelta(**options)


def create_error_response(base, **options) -> Dict[str, Any]:
    if len(options):
        return dict(base=base, args=options)
    else:
        return dict(base=base)


def create_error(status: STATUS, base: str, **option) -> Dict[str, Any]:
    return dict(error=create_error_response(base, **option), status=status)
