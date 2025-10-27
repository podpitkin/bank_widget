import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def return_amount(transaction: dict) -> float | None:
    """
    Функция возвращает сумму транзакции в рублях.
    Если валюта транзакции не рубли, то функция обращается к внешнему ресурсу
    для конвертации валюты транзакции в рубли
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    else:
        currency = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        payload = {}
        headers = {"apikey": api_key}
        try:
            response = requests.get(url, headers=headers, data=payload)
            if response.status_code in range(200, 299):
                result_amount = response.json()
                return result_amount["result"]
            else:
                return None
        except requests.RequestException:
            return None
        except (KeyError, json.JSONDecodeError):
            return None
