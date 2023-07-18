import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def item():
    return Item("Test Item", 100.0, 5)


@pytest.fixture
def phone():
    return Phone("Test Phone", 500.0, 10, 1)
