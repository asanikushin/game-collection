from json import JSONEncoder
import decimal


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        try:
            return o.get_dict()
        except AttributeError:
            pass
        if type(o) == decimal.Decimal:
            return str(o)
        return o.__dict__
