from utils.coders import parse_csv_row, my_int

from uuid import uuid4
from typing import List, Tuple, Optional
from lxml import etree


class Index:
    def __init__(self, name, categories, min_players, max_players):
        self.name = name
        self.categories = categories
        self.min_players = min_players
        self.max_players = max_players

    def parse_csv_row(self, row: str) -> Tuple[str, str, Optional[str], Optional[str]]:
        data = parse_csv_row(row)
        result = (
            data[self.name] if len(data) > self.name else "No name",
            data[self.categories] if len(data) > self.categories else "No category",
            data[self.min_players] if len(data) > self.min_players else None,
            data[self.max_players] if len(data) > self.max_players else None
        )
        return result

    @staticmethod
    def parse_from_header(header: str):
        data = parse_csv_row(header)
        return Index(data.index("name"), data.index("categories"), data.index("min_players"),
                     data.index("max_players"))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Index):
            return NotImplemented
        return self.name == other.name and self.categories == other.categories \
               and self.min_players == other.min_players and self.max_players == other.max_players

    def __repr__(self):
        return f"Index({self.name}, {self.categories}, {self.min_players}, {self.max_players})"


class BatchElement:
    def __init__(self, name: str, category: str, min_players=None, max_players=None):
        self.name = name
        self.category = category
        self._min_players = min_players
        self._max_players = max_players

    @staticmethod
    def from_csv_row(row: str, index: Index) -> "BatchElement":
        data = index.parse_csv_row(row)
        return BatchElement(data[0], data[1].split(" | ")[0], my_int(data[2]), my_int(data[3]))

    @staticmethod
    def from_xml_element(element: etree._Element) -> "BatchElement":
        name = value.text if (value := element.find("title")) is not None else "No name"
        category = value.text if (value := element.find("category")) is not None else "No category"
        min_players = value.text if (value := element.find("min_players")) is not None else None
        max_players = value.text if (value := element.find("max_players")) is not None else None

        return BatchElement(name, category, my_int(min_players), my_int(max_players))

    @property
    def min_players(self) -> int:
        return self._min_players if self._min_players else 0

    @property
    def max_players(self) -> int:
        return self._max_players if self._max_players else 0

    def get_dict(self):
        result = dict(name=self.name, category=self.category)
        result["min_players"] = self.min_players
        result["max_players"] = self.max_players
        return result

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BatchElement):
            return NotImplemented
        min_player = self.min_players == other.min_players
        max_player = self.max_players == other.max_players
        return self.name == other.name and self.category == other.category and min_player and max_player

    def __repr__(self):
        return f"BatchElement(\"{self.name}\", \"{self.category}\", {self.min_players}, {self.max_players})"


class BatchList:
    def __init__(self):
        self.list: List[BatchElement] = []
        self.id = uuid4()

    def add(self, element: BatchElement) -> "BatchList":
        self.list.append(element)
        return self

    def size(self) -> int:
        return len(self.list)

    def to_list(self) -> List[BatchElement]:
        return self.list

    def clear(self) -> None:
        self.list = []
        self.id = uuid4()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BatchList):
            return NotImplemented
        return self.size() == other.size() and self.list == other.list
