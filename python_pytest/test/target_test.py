from foo.target import *
import pytest

class Testスーパーの支払金額:
    @pytest.mark.parametrize('item_no, unit_price',
        [(1, 100), (2, 40), (3, 150), (4, 150),
         (5, 400), (6, 420), (7, 440), (8, 100),
         (9, 80), (10, 100)])
    def test_商品1個の単価を取り出す(self, item_no, unit_price):
        assert get_unit_price(item_no) == unit_price

    class Test複数の商品の合計金額:
        def test_1個だけの場合(self):
            assert get_subtotal_of_item([(1, 1)]) == 100

        def test_1商品複数個の場合(self):
            assert get_subtotal_of_item([(1, 3)]) == 300

        def test_2商品1個ずつの場合(self):
            assert get_subtotal_of_item([(1, 1), (4, 1)]) == 250

        def test_2商品複数個ずつの場合(self):
            assert get_subtotal_of_item([(8, 8), (5, 5)]) == 2800

    class Testタバコの取り扱い:
        def test_タバコは内税(self):
            assert get_subtotal_of_item_incl_tax([(6, 1)]) == 420

        class Test10個で1個オマケ:
            def test_11個の場合(self):
                assert get_subtotal_of_item_incl_tax([(6, 11)]) == 420 * 10

            def test_25個の場合(self):
                assert get_subtotal_of_item_incl_tax([(6, 25)]) == 420 * (25 - 2)

