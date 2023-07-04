import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item("Test Item", 100.0, 5)
