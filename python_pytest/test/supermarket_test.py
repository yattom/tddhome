import pytest

from foo.supermarket import *

@pytest.fixture
def cart():
    return Cart()

def test_checkout_items_りんご2個とのり弁1個で550円(cart):
    cart.add_item(1, 2)
    cart.add_item(4, 1)
    assert cart.total() == 550

class TestCart:
    def test_最初は空(self, cart):
        assert cart.total() == 0

    def test_存在しない商品IDなら例外(self, cart):
        cart = Cart()
        with pytest.raises(ValueError):
            cart.add_item(999, 1)

    def test_個数は自然数なら例外(self, cart):
        cart = Cart()
        with pytest.raises(ValueError):
            cart.add_item(1, 0)
