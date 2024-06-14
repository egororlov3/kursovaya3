import json


def open_file():
    """Возвращает файл json в виде списка"""
    with open('operations_new.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    print(data)

print(open_file)