from widget import get_date


def pattern(data):
    print('\nПрограмма: Распечатываю итоговый список транзакций...\n')
    print(f'Программа:\nВсего банковских операций в выборке: {len(data)}\n')
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
