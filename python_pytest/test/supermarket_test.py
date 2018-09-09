import pytest

from foo.supermarket import *

@pytest.fixture
def cart():
    return Cart()

def test_checkout_items_りんご2個とのり弁1個で550円(cart):
    cart.add_item(1, 2)
    cart.add_item(4, 1)
    assert cart.simple_total() == 550

def test_消費税込みの金額_りんご1個で108円(cart):
    cart.add_item(1, 1)
    assert cart.total() == 108

class TestCart:
    def test_最初は空(self, cart):
        assert cart.simple_total() == 0

    def test_存在しない商品IDなら例外(self, cart):
        cart = Cart()
        with pytest.raises(ValueError):
            cart.add_item(999, 1)

    def test_個数は自然数なら例外(self, cart):
        cart = Cart()
        with pytest.raises(ValueError):
            cart.add_item(1, 0)
