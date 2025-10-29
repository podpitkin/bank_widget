from typing import Generator, Iterator


def filter_by_currency(transactions: list, valuta: str) -> Generator:
    """Функция фильтрует транзакции по заданной в условии валюте"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == valuta:
            yield transaction


def transaction_descriptions(transactions: list) -> Generator:
    """Генератор формирует описания транзакций"""
    for transaction in transactions:
        description = transaction["description"]
        yield description


def card_number_generator(start: int, stop: int) -> Iterator:
    """Генерирует номера банковских карт в заданном диапазоне"""
    for card_number in range(start, stop + 1):
        card_number = f"{card_number:016d}"
        filter_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield filter_card_number
