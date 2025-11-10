import csv
import pandas as pd
import json


def read_csv(path):
    """Функция считывает файл формата .csv  """
    try:
        df = pd.read_csv(path)
        df_dict = df.to_dict('records')
        return json.dumps(df_dict, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        return []


def read_excel(path):
    """Функция считывает файл формата .excel  """
    try:
        df = pd.read_excel(path)
        df_dict = df.to_dict('records')
        return json.dumps(df_dict, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        return []

# print(read_csv('../data/transactions.csv'))
# print(read_excel('../data/transactions_excel.xlsx'))