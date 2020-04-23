from json import JSONEncoder
import decimal
import uuid


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
