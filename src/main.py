from description import process_bank_search, process_bank_operations
from generators import filter_by_currency
from processing import filter_by_state, sort_by_date
from utils import read_file
import pandas as pd
from widget import mask_account_card, get_date



def main():
    """ Функция, которая отвечает за логику проекта и связывает функциональности между собой """
    input_user = int(input('''
Программа: Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла

 Пользователь: '''))
    if input_user == 1:
        print('\nПрограмма: Для обработки выбран JSON-файл.\n')
        data = read_file('../data/operations.json')
    elif input_user == 2:
        print('\nПрограмма: Для обработки выбран CSV-файл.\n')
        df = pd.read_csv('../data/transactions.csv')
        json_data = df.to_json(orient='records', force_ascii=False, indent=2)
        with open('../data/csv_js.json', 'w', encoding='utf-8') as f:
            f.write(json_data)
        data = read_file('../data/ex_js.json')
    elif input_user == 3:
        print('\nПрограмма: Для обработки выбран XLSX-файл.\n')
        df = pd.read_excel('../data/transactions_excel.xlsx')
        json_data = df.to_json(orient='records', force_ascii=False, indent=2)
        with open('../data/ex_js.json', 'w', encoding='utf-8') as f:
            f.write(json_data)
        data = read_file('../data/ex_js.json')
    else:
        print(f'Программа: Некорректный ввод. Завершение программы')
        return

    statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        input_status = input('''
Программа: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

 Пользователь: ''').upper()
        if input_status.upper() in statuses:
            data = filter_by_state(data, input_status)
            break
        print(f'Программа: Статус операции "{input_status}" недоступен.')

    while True:
        sort_date_input = input('''
Программа: Отсортировать операции по дате? Да/Нет

 Пользователь: ''').lower()
        if sort_date_input in ['да', 'нет']:
            break
        else:
            print(f'Программа: "{sort_date_input}" - недопустимый ввод. Введите Да или Нет.')

    if sort_date_input == 'да':
        while True:
            choice_input = input('''
Программа: Отсортировать по возрастанию или по убыванию?

 Пользователь: ''').lower()
            if choice_input in ['по возрастанию', 'по убыванию']:
                dec = choice_input == 'по убыванию'
                data = sort_by_date(data, dec)
                break

    while True:
        rub_transaction = input('''
Программа: Выводить только рублевые транзакции? Да/Нет

 Пользователь: ''').lower()
        if rub_transaction in ['да','нет']:
            break
    if rub_transaction == 'да':
        data = filter_by_currency(data,'RUB')

    while True:
        word_filter = input('''
Программа: Отфильтровать список транзакций по определенному слову
в описании? Да/Нет

 Пользователь: ''').lower()
        if word_filter in ['да','нет']:
            break
    if word_filter == 'да':
        search_word = input('Программа: Введите слово для поиска: ').lower()
        data = process_bank_search(data, search_word)

    filter_data = []
    for transaction in data:

        from_value = transaction.get('from')  # тут я проверила пустое ли поле from в файлах
        if from_value:
            transaction['from'] = mask_account_card(from_value)

        to_value = transaction.get('to')
        if to_value:
            transaction['to'] = mask_account_card(to_value)

        filter_data.append(transaction)
    data = filter_data
    if data == []:
        print('Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
    if data != []:
        print('Программа: Распечатываю итоговый список транзакций...')
        print(f'Программа:Всего банковских операций в выборке: {len(data)}\n')
        for transaction in data:
            if 'operationAmount' in transaction:
                amount = transaction['operationAmount']['amount']
                currency_name = transaction['operationAmount'].get('currency', {}).get('name')
            else:
                amount = transaction['amount']
                currency_name = transaction.get('currency_code')
            date_obj = transaction.get('date')
            date = get_date(date_obj)
            description = transaction.get('description')
            from_account = transaction.get('from')
            to_account = transaction.get('to')


            print(f'{date} {description}')
            if from_account and to_account:
                print(f'{from_account} -> {to_account}')
            elif to_account:
                print(f'{to_account}')
            print(f'Сумма: {amount} {currency_name}\n')

# if __name__ == '__main__':
#     print(main())