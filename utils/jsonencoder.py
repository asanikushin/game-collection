from json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        try:
            return o.get_dict()
        except AttributeError:
            pass
        return o.__dict__
