from utils.coders import parse_csv_row, my_int

import typing
from uuid import uuid4
from typing import List


class Index:
    def __init__(self, name, categories, min_players, max_players):
        self.name = name
        self.categories = categories
        self.min_players = min_players
        self.max_players = max_players

    def parse_csv_row(self, row: str) -> List:
        row = parse_csv_row(row)
        result = [
            row[self.name] if len(row) > self.name else "No name",
            row[self.categories] if len(row) > self.categories else "No category",
            row[self.min_players] if len(row) > self.min_players else None,
            row[self.max_players] if len(row) > self.max_players else None
        ]
        return result

    @staticmethod
    def parse_from_header(header: List):
        return Index(header.index("name"), header.index("categories"), header.index("min_players"),
                     header.index("max_players"))

    def __eq__(self, other: "Index"):
        return self.name == other.name and self.categories == other.categories \
               and self.min_players == other.min_players and self.max_players == other.max_players

    def __repr__(self):
        return f"Index({self.name}, {self.categories}, {self.min_players}, {self.max_players})"


class BatchElement:
    def __init__(self, name, category, min_players=None, max_players=None):
        self.name = name
        self.category = category
        self._min_players = min_players
        self._max_players = max_players

    @staticmethod
    def from_row(row: str, index: Index):
        data = index.parse_csv_row(row)
        return BatchElement(data[0], data[1].split(" | ")[0], my_int(data[2]), my_int(data[3]))

    @property
    def min_players(self):
        return self._min_players if self._min_players else 0

    @property
    def max_players(self):
        return self._max_players if self._max_players else 0

    def get_dict(self):
        result = dict(name=self.name, category=self.category)
        result["min_players"] = self.min_players
        result["max_players"] = self.max_players
        return result

    def __eq__(self, other: "BatchElement"):
        min_player = self.min_players == other.min_players
        max_player = self.max_players == other.max_players
        return self.name == other.name and other.category and min_player and max_player

    def __repr__(self):
        return f"BatchElement(\"{self.name}\", \"{self.category}\", {self.min_players}, {self.max_players})"


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
