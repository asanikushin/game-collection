from utils.queues.models import BatchElement, BatchList, Index

import pytest
import pickle


def test_index_parser():
    value = Index.parse_from_header("name,categories,min_players,max_players")
    assert value == Index(0, 1, 2, 3)

    value = Index.parse_from_header(
        "id,name,year,categories,families,max_players,mechanics,min_players"
    )
    assert value == Index(1, 3, 7, 5)

    value = Index.parse_from_header(
        "id,name,year,artists,categories,families,max_players,mechanics,min_age,min_players"
    )
    assert value == Index(1, 4, 9, 6)

    with pytest.raises(ValueError):
        Index.parse_from_header("name,categories,min_players")


def test_batch_csv():
    index = Index(1, 3, 7, 5)

    value = BatchElement.from_csv_row(
        "307679,Billionaire,1973,Economic,,4,Auction/Bidding,2", index
    )
    assert value == BatchElement("Billionaire", "Economic", 2, 4)

    value = BatchElement.from_csv_row(
        "145,Metropolis,1984,City Building | Negotiation,,5,,2", index
    )
    assert value == BatchElement("Metropolis", "City Building", 2, 5)

    value = BatchElement.from_csv_row("22044,ZIN,1994,Abstract Strategy", index)
    assert value == BatchElement("ZIN", "Abstract Strategy", 0, 0)

    value = BatchElement.from_csv_row("22044,ZIN,1994,Abstract Strategy,,,,4", index)
    assert value == BatchElement("ZIN", "Abstract Strategy", 4, 0)


def test_batch_list():
    count = 6
    array = BatchList()
    data = []
    for i in range(count):
        array.add(BatchElement(f"name_{i}", f"cat_{i}"))
        data.append(BatchElement(f"name_{i}", f"cat_{i}"))
    converted = pickle.loads(pickle.dumps(array))

    assert array.size() == count
    assert array.to_list() == data
    assert array == converted

    array.clear()
    assert array.size() == 0
