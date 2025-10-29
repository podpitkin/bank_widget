import json
import logging


logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_file(path):
    """Функция, которая читает json файл"""
    logger.debug("Начало работы функции")
    try:
        logger.debug("Открытие json-файла")
        with open(path, "r", encoding="utf-8") as json_file:
            try:
                data = json.load(json_file)
            except json.JSONDecodeError as ex:
                logger.error(f"Невалидный json файл. Ошибка: {ex}")
                return []
    except FileNotFoundError:
        return []
    logger.debug("Завершение работы функции")
    return data
