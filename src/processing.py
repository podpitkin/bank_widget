def filter_by_state(dict_list: list, state: list = "EXECUTED") -> list:
    """Функция, которая возвращает значениe по ключу"""
    new_dict = []
    for dict in dict_list:
        if dict.get("state") == state:
            new_dict.append(dict)

    return new_dict


def sort_by_date(list_date: list, reverse=True) -> list:
    """Функция, которая сортирует список по дате"""
    sort_date = sorted(list_date, key=lambda x: x["date"], reverse=reverse)

    return sort_date
