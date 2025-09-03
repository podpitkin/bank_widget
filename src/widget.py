from masks import get_mask_account, get_mask_card_number


def mask_account_card(name_num_card: str) -> str:
    """Функция, которая обрабатывает информацию о картах или счетах счетах"""
    card_split = name_num_card.rsplit(" ", 1)
    num_card = card_split[1]
    if card_split[0] == "Счет":
        return f"{card_split[0]} {get_mask_account(num_card)}"
    else:
        return f"{card_split[0]} {get_mask_card_number(num_card)}"


def get_date(filter_date: str) -> str:
    """Функция, которая преображает формат даты"""
    return f"{filter_date[8:10]}.{filter_date[5:7]}.{filter_date[0:4]}"
