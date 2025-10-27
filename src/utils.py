import json


def read_file(path):
    """Функция, которая читает json файл"""
    try:
        with open(path, "r", encoding="utf-8") as json_file:
            try:
                data = json.load(json_file)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    return data


# Тест
# print(read_file('../data/operations.json'))
