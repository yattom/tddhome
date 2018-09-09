import pytest

from foo.supermarket import *

@pytest.fixture
def cart():
    return Cart()


def test_複数品目複数個の計算ができる(cart):
    cart.add_item(1, 2)
    cart.add_item(2, 3)
    cart.add_item(4, 1)
    assert cart.total() == 723 == int((100 * 2 + 40 * 3 + 350) * 1.08)


class Test消費税と内税:
    @pytest.mark.parametrize('item_id, amount, subtotal', [
        pytest.param(1, 1, 108, id="りんご1個で108円"),
        pytest.param(2, 1, 43, id="みかん1個で43円"),
        pytest.param(2, 4, 172, id="みかん4個で172円"),
    ])
    def test_消費税込みの金額(self, cart, item_id, amount, subtotal):
        cart.add_item(item_id, amount)
        assert cart.total() == subtotal

    def test_消費税込みの金額_タバコは内税なので420円(self, cart):
        cart.add_item(6, 1)
        assert cart.total() == 420


@pytest.mark.parametrize('amount, subtotal', [
    (3, int(280 * 1.08)),
    (4, int((280 + 100) * 1.08)),
    (10, int((280 * 3 + 100)* 1.08)),
])
def test_リンゴは1個100円だが3つ買うと280円になる(cart, amount, subtotal):
    cart.add_item(1, amount)
    assert cart.total() == subtotal


class TestCart:
    def test_最初は空(self, cart):
        assert cart.total() == 0
        assert cart.get_item_amount(1) == 0

    def test_存在しない商品IDなら例外(self, cart):
        with pytest.raises(ValueError):
            cart.add_item(999, 1)

    def test_個数は自然数なら例外(self, cart):
        with pytest.raises(ValueError):
            cart.add_item(1, 0)

    def test_同じ商品IDを複数回に分けて追加してもまとまる(self, cart):
        cart.add_item(1, 1)
        cart.add_item(1, 2)
        cart.add_item(1, 3)
        assert 6 == cart.get_item_amount(1)

