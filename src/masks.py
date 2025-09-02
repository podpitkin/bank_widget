def get_mask_card_number(num_card: int) -> str:
    """Функция, которая вовращает номер карты ввиде ХХХХ ХХ** **** ХХХХ"""
    num_card = str(num_card)
    if len(num_card) == 16:
        mask_card = f"{num_card[:4]} {num_card[4:6]}** **** {num_card[-4:]}"
        return mask_card
    return "Некорректный ввод"


def get_mask_account(acc_num: int) -> str:
    """Функция, которая возвращает номер счета ввиде **ХХХХ"""
    acc_num = str(acc_num)
    if len(acc_num) >= 4:
        mask_acc = f"**{acc_num[-4:]}"
        return mask_acc
    return "Некорректный ввод"
