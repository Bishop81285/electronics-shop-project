"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item_init():
    item = Item("Test Item", 100.0, 5)

    assert item.name == "Test Item"
    assert item.price == 100.0
    assert item.quantity == 5
    assert item in Item.all


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 500.0


def test_apply_discount(item):
    Item.pay_rate = 0.5
    item.apply_discount()

    assert item.price == 50.0
