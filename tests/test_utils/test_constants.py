from utils.constants import responses, statuses

import pytest


@pytest.mark.parametrize(
    "skip_statuses",
    [{"internal"}, pytest.param(set(), marks=pytest.mark.xfail(strict=True))],
)
def test_http_status(skip_statuses):
    if skip_statuses is None:
        skip_statuses = set()
    bad = []
    all_keys = set(responses.keys())
    for key, value in statuses.items():
        if key in skip_statuses:
            continue
        for sub_key, status in value.items():
            if status in all_keys:
                all_keys.remove(status)
            if (key, sub_key) in skip_statuses:
                continue
            if status not in responses:
                bad.append((key, sub_key))

    assert all_keys == set()
    assert bad == []


def test_check_statuses():
    inverse_status = dict()
    bad = set()
    for key, value in statuses.items():
        for sub_key, status in value.items():
            old = []
            if status in inverse_status:
                bad.add(status)
                old = inverse_status[status]
            inverse_status[status] = old + [(key, sub_key)]

    duplicate = dict()
    for status in bad:
        duplicate[status] = inverse_status[status]
    assert duplicate == {}
