import json


def open_file():
    """Возвращает файл json в виде списка"""
    with open('operations_new.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_executed_operations(data):
    """Возвращает выполненные операции"""
    executed_data = data
    for d in data:
        for k, v in d.items():
            if k == "state" and v == "EXECUTED":
                return data
    return executed_data


    # пройти в цикл по списку
    # обротиться к ключу state
    # сравнить равен ли state == EXECUTED, если равен добавить в новый список


def sort_operations(data):
    """Возращает пять последних выполненных операций"""
    # todo отсортировать по дате методом sort или sorted
    last_dates = data
    for a in data:
        if a == data:
            return data
    return last_dates[:5]


def day_of_operation(data):
    """Получение даты операции"""
    date_of_operations = data
    for key, value in data.items():
        if key != "date":
            return value
    return date_of_operations


def description_of_operation(data):
    """Получение информации о том какая была операция"""
    info_of_operations = data
    for key, value in data.items():
        if key != "description":
            return value
    return info_of_operations


def card_from(data):
    """Карта/счет отправителя"""
    operations_from = data
    for key, value in data.items():
        if key != "from":
            return value
    return operations_from


def card_to(data):
    """Карта/счет получателя"""
    operations_to = data
    for key, value in data.items():
        if key != "to":
            return value
    return operations_to


def sum_of_operation(data):
    """Сумма операции"""
    operations_sum = data
    for key, value in data.items():
        if key != "amount":
            return value
    return operations_sum


def currency(data):
    """Валюта операции"""
    currency_of_operations = data
    for key, value in data.items():
        if key != "code":
            return value
    return currency_of_operations
