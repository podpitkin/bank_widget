import pytest
from generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(trans):
    result = list(filter_by_currency(trans, "USD"))
    expected = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    assert result == expected


def test_transaction_descriptions(trans):
    descriptions = list(transaction_descriptions(trans))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

    assert len(descriptions) == len(expected)
    assert descriptions == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (0, 2, ["0000 0000 0000 0000", "0000 0000 0000 0001", "0000 0000 0000 0002"]),
    ],
)
def test_card_number_generator(start, end, expected):
    generated_numbers = list(card_number_generator(start, end))
    assert generated_numbers == expected


def test_card_num_generator(card_num):
    assert len(card_num) == 16, "Номер карты некорректной длины"
    assert card_num.isdigit(), "Номер карты содержит нецифровые символы"
