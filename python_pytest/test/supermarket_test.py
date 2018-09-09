import pytest

from foo.supermarket import *

@pytest.fixture
def cart():
    return Cart()

def test_消費税込みの金額_りんご1個で108円(cart):
    cart.add_item(1, 1)
    assert cart.total() == 108

def test_消費税込みの金額_小数点以下切り捨て_みかん1個で43円(cart):
    cart.add_item(2, 1)
    assert cart.total() == 43

def test_消費税込みの金額_小数点以下切り捨て_みかん4個で172円(cart):
    cart.add_item(2, 4)
    assert cart.total() == 172 == (40 * 4) + int(40 * 4 * 0.08)

def test_消費税込みの金額_タバコは内税なので420円(cart):
    cart.add_item(6, 1)
    assert cart.total() == 420

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
