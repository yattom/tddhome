from foo.target import get_unit_price

def test_商品番号1から単価100を取り出す():
    assert get_unit_price(1) == 100

def test_商品番号2から単価40を取り出す():
    assert get_unit_price(2) == 40

def test_商品番号3から単価150を取り出す():
    assert get_unit_price(3) == 150

