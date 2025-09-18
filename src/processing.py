def filter_by_state(dict_list: list, state: list = "EXECUTED") -> list:
    """Функция, которая возвращает значениe по ключу"""
    new_dict = []
    for dict in dict_list:
        if dict.get("state") == state:
            new_dict.append(dict)

    return new_dict


def sort_by_date(dict_list: list, reverse: bool = True) -> list:
    """Функция, которая сортирует список по дате"""
    sort_date = sorted(dict_list, key=lambda x: x["date"], reverse=True)

    return sort_date
i = sort_by_date([
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ])
print(i)