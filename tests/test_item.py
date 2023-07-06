"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

import pytest

from src.item import Item


def test_item_init():
    item = Item("Test Item", 100.0, 5)

    assert item.name == "Test Item"  # Property
    assert item.price == 100.0
    assert item.quantity == 5
    assert item in Item.all


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 500.0


def test_apply_discount(item):
    Item.pay_rate = 0.5
    item.apply_discount()

    assert item.price == 50.0


def test_name_setter_valid_length(item):
    item.name = 'Test Name'
    assert item.name == 'Test Name'


def test_name_setter_invalid_length(item):
    with pytest.raises(Exception) as exception_info:
        item.name = "Very Long Name"

    assert str(exception_info.value) == 'Длина наименования товара превышает 10 символов.'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv(tmp_path):
    csv_path = tmp_path / "test.csv"
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["name", "price", "quantity"])
        writer.writerow(["Item1", "250", "2"])
        writer.writerow(["Item2", "300", "10"])

    Item._Item__csv_path = str(csv_path)
    Item.all = []

    Item.instantiate_from_csv()

    assert len(Item.all) == 2
    assert Item.all[0].name == "Item1"
    assert Item.all[0].price == "250"
    assert Item.all[0].quantity == "2"
    assert Item.all[1].name == "Item2"
    assert Item.all[1].price == "300"
    assert Item.all[1].quantity == "10"
