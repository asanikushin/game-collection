from json import JSONEncoder
import decimal
import uuid
from typing import List, Optional


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        try:
            return o.get_dict()
        except AttributeError:
            pass
        if type(o) == decimal.Decimal:
            return str(o)
        if type(o) == uuid.UUID:
            return str(o)
        return o.__dict__


def parse_csv_row(row: str) -> List:
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
    result.append(cur)
    return result


def my_int(val: Optional[str]) -> int:
    if val is None or val == "":
        return 0
    return int(val)
