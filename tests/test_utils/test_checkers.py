from utils.checkers import check_email, check_keys


def test_email_checker():
    value = check_email("tester@domain")
    assert value == "tester@domain"

    value = check_email("tester")
    assert value is None

    value = check_email("@domain")
    assert value is None


def test_key_checker_strict():
    converted = {key: key for key in ["first", "second", "third"]}

    assert check_keys(converted, "first", strict=True)
    assert check_keys(converted, "first", "second", strict=True)
    assert not check_keys(converted, "last", strict=True)


def test_key_checker_not_strict():
    converted = {key: key for key in ["first", "second", "third"]}

    assert check_keys(converted, "first", strict=False)
    assert check_keys(converted, "first", "second", strict=False)

    assert not check_keys(converted, "last", strict=False)
    assert check_keys(converted, "first", "last", strict=False)
