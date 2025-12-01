from collections import Counter
from description import process_bank_search, process_bank_operations


def test_process_bank_search(data):
    result = process_bank_search(data, "вклад")
    expected = [
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {
                "amount": "79931.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215"
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        },
    ]
    assert result == expected


def test_process_bank_operation(data):
    categories = ("Открытие вклада", "Перевод организации")
    result = process_bank_operations(data, categories)
    expected = Counter({"Перевод организации": 1, "Открытие вклада": 2})
    assert result == expected
