import logging


logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(num_card: str) -> str:
    """Функция, которая возвращает номер карты в виде ХХХХ ХХ** **** ХХХХ"""
    logger.debug(f"Ввод карты: {num_card}")
    num_card = str(num_card)
    if len(num_card) == 16:
        mask_card = f"{num_card[:4]} {num_card[4:6]}** **** {num_card[-4:]}"
        logger.debug(f"Маскировка вводимой карты {mask_card}")
        return mask_card
    logger.error("ВВели некорректный номер карты")
    return "Некорректный ввод"


def get_mask_account(acc_num: str) -> str:
    """Функция, которая возвращает номер счета в виде **ХХХХ"""
    logger.debug(f"Ввод номера счета {acc_num}")
    acc_num = str(acc_num)
    if len(acc_num) >= 4:
        mask_acc = f"**{acc_num[-4:]}"
        logger.debug(f"Маскировка счета {mask_acc}")
        return mask_acc
    logger.error("Ввели некорректный номер счета")
    return "Некорректный ввод"
