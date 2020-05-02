from utils.coders import parse_timedelta, parse_csv_row
import pytest
from datetime import timedelta


@pytest.mark.parametrize("delta, parsed", [
    ("5W", timedelta(weeks=5)),
    ("5m", timedelta(minutes=5)),
    ("5M 3H 1S", timedelta(minutes=5, hours=3, seconds=1)),
    pytest.param("5q", timedelta(weeks=5), marks=pytest.mark.xfail(strict=True))
])
def test_time_parser(delta, parsed):
    value = parse_timedelta(delta)
    assert value == parsed


@pytest.mark.parametrize("value, parsed", [
    ("name,categories,min_players,max_players", ['name', 'categories', 'min_players', 'max_players']),
    ("name,\"comma, row\"", ["name", "comma, row"]),
    ("", [""])
])
def test_csv_parser(value, parsed):
    result = parse_csv_row(value)
    assert result == parsed
