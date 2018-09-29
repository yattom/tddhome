from foo.calc import Calc
import pytest

@pytest.fixture
def calc():
    return Calc()

class Test引き算:
    def test_引き算_3引く1(self, calc):
        assert 2 == calc.sub(3, 1)

    def test_引き算_4引く3(self, calc):
        assert 1 == calc.sub(4, 3)

class Test引き算:
    def test_割り算_1割る1(self, calc):
        assert 1 == calc.div(1, 1)

    def test_割り算_4割る2(self, calc):
        assert 2 == calc.div(4, 2)

    def test_割り算_0割る0_例外(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.div(0, 0)

