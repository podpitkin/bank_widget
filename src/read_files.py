import csv
import pandas as pd


def read_csv(path):
    """Функция считывает файл формата .csv  """
    try:
        with open(path, encoding="utf-8") as file:
            reader_csv = csv.DictReader(file)
            return reader_csv
    except FileNotFoundError:
        return []


def read_excel(path):
    """Функция считывает файл формата .excel  """
    try:
        df = pd.read_excel(path)
        return df
    except FileNotFoundError:
        return []
