from utils.coders import parse_timedelta, parse_csv_row, create_error_response
import pytest
from datetime import timedelta


def test_time_parser():
    value = parse_timedelta("5W")
    assert value == timedelta(weeks=5)

    value = parse_timedelta("5m")
    assert value == timedelta(minutes=5)

    value = parse_timedelta("5M 3H 1S")
    assert value == timedelta(minutes=5, hours=3, seconds=1)

    with pytest.raises(ValueError):
        parse_timedelta("5q")


def test_csv_parser():
    value = parse_csv_row("name,categories,min_players,max_players")
    assert value == ["name", "categories", "min_players", "max_players"]

    value = parse_csv_row('name,"comma, row"')
    assert value == ["name", "comma, row"]

    value = parse_csv_row("value")
    assert value == ["value"]

    value = parse_csv_row(",")
    assert value == ["", ""]

    value = parse_csv_row("")
    assert value == []


def test_error_response():
    assert len(create_error_response("base error")) == 1

    error_with_arg = create_error_response("some base", arg1="first")
    assert len(error_with_arg) == 2
    assert len(error_with_arg["args"]) == 1

    error_with_args = create_error_response("some base", arg1="first", arg2="second")
    assert len(error_with_args) == 2
    assert len(error_with_args["args"]) == 2
