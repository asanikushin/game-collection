from utils.coders import parse_csv_row

import typing
from uuid import uuid4


class BatchElement:
    def __init__(self, name, category, min_players=None, max_players=None):
        self.name = name
        self.category = category
        self.min_players = min_players
        self.max_players = max_players

    @staticmethod
    def from_row(row: str, index: list):
        row = parse_csv_row(row)
        name = row[index[0]] if len(row) > index[0] else "No name"
        category = split[0] if len(row) > index[1] and (split := row[index[1]].split(" | ")) else "No category"
        min_players = int(row[index[2]]) if len(row) > index[2] else 0
        max_players = int(row[index[3]]) if len(row) > index[3] else 0

        return BatchElement(name, category, min_players, max_players)

    def get_dict(self):
        result = dict(name=self.name, category=self.category)
        result["min_players"] = self.min_players if self.min_players else 0
        result["max_players"] = self.max_players if self.max_players else 0
        return result


class BatchList:
    def __init__(self):
        self.list: typing.List[BatchElement] = []
        self.id = uuid4()

    def add(self, element: BatchElement) -> "BatchList":
        self.list.append(element)
        return self

    def size(self) -> int:
        return len(self.list)

    def to_list(self) -> typing.List[BatchElement]:
        return self.list

    def clear(self):
        self.list: typing.List[BatchElement] = []
        self.id = uuid4()
