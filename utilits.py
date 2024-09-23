import json
from datetime import datetime


def open_file():
    """Возвращает файл json в виде списка"""
    with open('operations_new.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_executed_operations(data):
    """Возвращает выполненные операции"""
    return [operation for operation in data if operation["state"] == "EXECUTED"]


def sort_operations(data):
    """Возвращает пять последних выполненных операций"""
    last_five = sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=True)
    return last_five[:5]


def format_operation(data):
    """Изменяет формат даты операций на ДД.ММ.ГГГГ"""
    for operation in data:
        date_str = operation["date"]
        date_obj = datetime.fromisoformat(date_str)
        formatted_date = date_obj.strftime("%d.%m.%Y")
        operation["date"] = formatted_date


def mask_card_number(card_number):
    """Маскировка номера карты"""
    card_number = card_number.replace(" ", "")
    if len(card_number) < 16:
        return card_number

    # Замаскируем номер карты, показывая только первые 6 и последние 4 цифры
    masked_number = f"{card_number[:6]}******{card_number[-4:]}"
    return masked_number


def mask_account_number(account_number):
    """Маскировка номера счета"""
    return f"**{account_number[-4:]}" if len(account_number) >= 4 else account_number


def print_operations(data):
    """Выводит последние пять выполненных операций в заданном формате."""
    for operation in data:
        date = operation["date"]
        description = operation["description"]

        from_account = operation.get("from", "Счет")
        to_account = operation.get("to", "Счет")

        amount = operation["operationAmount"]["amount"]
        currency = operation["operationAmount"]["currency"]["name"]

        # Замаскируем номера карт/счетов
        if any(card in from_account for card in ["Maestro", "Visa", "MasterCard"]):
            card_type = from_account.split()[0]
            card_number = from_account[len(card_type):].strip()
            masked_from = f"{card_type} {mask_card_number(card_number)}"
        else:
            masked_from = mask_account_number(from_account)

        masked_to = mask_account_number(to_account) if "Счет" in to_account else mask_card_number(to_account)

        # Формируем строку для вывода
        output_line = (
            f"{date} {description}\n"
            f"{masked_from} -> {masked_to}\n"
            f"{amount} {currency}"
        )
        print(output_line)
        print()
