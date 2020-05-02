from utils.queues.models import BatchElement, Index

import pytest


@pytest.mark.parametrize("header, index", [
    ("name,categories,min_players,max_players", Index(0, 1, 2, 3)),
    ("id,name,year,categories,families,max_players,mechanics,min_players", Index(1, 3, 7, 5)),
    ("id,name,year,artists,categories,families,max_players,mechanics,min_age,min_players", Index(1, 4, 9, 6)),
])
def test_index_parser(header, index: Index):
    value = Index.parse_from_header(header)
    assert value == index


@pytest.mark.parametrize("row, element", [
    ('307679,Billionaire,1973,Economic,,4,Auction/Bidding,2', BatchElement('Billionaire', 'Economic', 2, 4)),
    ('145,Metropolis,1984,City Building | Negotiation,,5,,2', BatchElement("Metropolis", "City Building", 2, 5)),
    ('22044,ZIN,1994,Abstract Strategy', BatchElement("ZIN", "Abstract Strategy", 0, 0)),
    ('22044,ZIN,1994,Abstract Strategy,,,,4', BatchElement("ZIN", "Abstract Strategy", 4, 0)),
])
@pytest.mark.parametrize("index", [Index(1, 3, 7, 5)])
def test_batch_csv(row, element: BatchElement, index: Index):
    value = BatchElement.from_row(row, index)
    assert value == element
