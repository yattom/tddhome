import pytest
from foo.range import Range


@pytest.fixture
def rng():
    return Range()


class Test整数閉区間オブジェクト:
    class Test上端点を設定できる:
        def test_8(self, rng):
            assert rng.set_upper(8).upper() == 8

        def test_0(self, rng):
            assert rng.set_upper(0).upper() == 0

        class Test上端点より下端点が大きいと例外になる:
            def test_下端点10で上端点8(self, rng):
                with pytest.raises(ValueError):
                    rng.set_lower(10).set_upper(8)

        def test_上書きはできない(self, rng):
            with pytest.raises(RuntimeError):
                rng.set_upper(8).set_upper(0)

    class Test下端点を設定できる:
        def test_3(self, rng):
            assert rng.set_upper(8).set_lower(3).lower() == 3

        class Test上端点より下端点が大きいと例外になる:
            def test_上端点0で下端点3だと例外(self, rng):
                with pytest.raises(ValueError):
                    rng.set_upper(0).set_lower(3)

        def test_上書きはできない(self, rng):
            with pytest.raises(RuntimeError):
                rng.set_lower(3).set_lower(-5)

    @pytest.mark.parametrize(
        "lower, upper, expected",
        [
            (3, 8, "[3,8]"),
            (-5, 0, "[-5,0]"),
        ]
    )
    def test_文字列表記を返せる(self, rng, lower, upper, expected):
        assert str(rng.set_upper(upper).set_lower(lower)) == expected


    class Test上端点のみの文字列表記を返せる:
        def test_上端点8の文字列表記(self, rng):
            assert str(rng.set_upper(8)) == "[-,8]"

    class Test下端点のみの文字列表記を返せる:
        def test_下端点3の文字列表記(self, rng):
            assert str(rng.set_lower(3)) == "[3,-]"

    def test_上端も下端もない文字列表記(self, rng):
        assert str(rng) == "[-,-]"
