import re
from collections import Counter
import pandas as pd

file = r"../data/transactions_excel.xlsx"
transactions_df = pd.read_excel(file)
trans_xl = transactions_df.to_dict(orient="records")


def process_bank_search(data, search_string):
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка"""
    result = []
    for operation in data:
        description = str(operation["description"])
        if re.search(search_string, description, flags=re.IGNORECASE):
            result.append(operation)
    return result


# filtered_transactions = process_bank_search(trans_xl, "перевод с карты")
# print(filtered_transactions)


def process_bank_operations(data, categories):
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество
    операций в каждой категории.
    """
    counter_category = Counter()
    for operation in data:
        description = operation.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                counter_category[category] += 1
    return counter_category
