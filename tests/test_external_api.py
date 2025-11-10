import pytest
from src.external_api import return_amount
from unittest.mock import patch
import os
from dotenv import load_dotenv


@patch('src.external_api.requests.get')
def test_return_amount(mocked_get):
    transaction = {
        "operationAmount": {
            "currency": {"code": "USD"},
            "amount": 1
        }
    }
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    payload = {}
    headers = {"apikey": os.getenv("API_KEY")}
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {"result": 2}
    result = return_amount(transaction)
    assert result == 2
    mocked_get.assert_called_once_with(
        url,
        headers=headers,
        data=payload
    )