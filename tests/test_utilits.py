import json
from unittest.mock import patch

import pytest
from datetime import datetime
from utilits import (
    open_file,
    get_executed_operations,
    sort_operations,
    mask_card_number,
    mask_account_number,
    format_operation, print_operations,
)
from test_data import TEST_DATA


@pytest.fixture
def temp_file(tmp_path):
    # Создаем временный файл и записываем тестовые данные
    file_path = tmp_path / "operations_new.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(TEST_DATA, f)
    return file_path


def test_open_file(temp_file):
    data = open_file()
    assert len(data) == 9
    assert data[0]["state"] == "CANCELED"


def test_get_executed_operations(temp_file):
    data = open_file()
    executed_operations = get_executed_operations(data)
    assert len(executed_operations) == 7
    assert executed_operations[0]["state"] == "EXECUTED"  #


def test_sort_operations(temp_file):
    data = open_file()
    sorted_operations = sort_operations(data)
    assert len(sorted_operations) == 5
    assert sorted_operations[1]["state"] == "EXECUTED"


def test_mask_card_number():
    assert mask_card_number("Maestro 1234567812345678") == "Maestr******5678"
    assert mask_card_number("Visa 1234567890123456") == "Visa12******3456"
    assert mask_card_number("1234") == "1234"


def test_mask_account_number():
    assert mask_account_number("1234567890123456") == "**3456"
    assert mask_account_number("123") == "123"


def test_format_operation():
    data = {"date": "2019-08-26T10:50:58.294041"}
    format_operation([data])
    assert data["date"] == "26.08.2019"


@patch('builtins.print')
def test_print_operations(mock_print):
    print_operations(TEST_DATA)

    # Выводим все вызовы print для отладки
    for call in mock_print.call_args_list:
        print(call)

    assert mock_print.call_count == 4  # Два вывода для операций и четыре пустых строки

    expected_output = (
        "26.08.2019 Перевод организации\n"
        "Maestro 159683******5199 -> Счет **8947\n"
        "31957.58 руб."
    )
    mock_print.assert_any_call(expected_output)
