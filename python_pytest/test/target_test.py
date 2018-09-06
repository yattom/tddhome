import pytest
from foo import target


class Test_FizzBuzz変換:
    @pytest.mark.parametrize('i,s', [(1, "1"), (2, "2")])
    def test_数はそのままにする_x(self, i, s):
        assert target.fizzbuzz(i) == s

    @pytest.mark.parametrize('i', [3, 9])
    def test_3の倍数のときは数の代わりにFizzにする(self, i):
        assert target.fizzbuzz(i) == "Fizz"

    @pytest.mark.parametrize('i', [5, 25])
    def test_5の倍数ときは数の代わりにBuzzにする(self, i):
        assert target.fizzbuzz(i) == "Buzz"

    @pytest.mark.parametrize('i', [15, 30])
    def test_3と5の倍数ときは数の代わりにFizzBuzzにする(self, i):
        assert target.fizzbuzz(i) == "FizzBuzz"

    @pytest.mark.parametrize('i,s', [
        pytest.param(1, "1", id="そのままの場合"),
        pytest.param(2, "2", id="そのままの場合"),
        pytest.param(3, "Fizz", id="3の倍数はFizz"),
        pytest.param(9, "Fizz", id="3の倍数はFizz"),
        pytest.param(5, "Buzz", id="5の倍数はBuzz"),
        pytest.param(15, "FizzBuzz", id="15の倍数はFizzBuzz")])
    def test_FizzBuzzにする_x(self, i, s):
        assert target.fizzbuzz(i) == s

def test_プリントする_1まで(capsys):
    target.fizzbuzz_run(1)
    s, _ = capsys.readouterr()
    assert s == "1\n"

def test_プリントする_5まで(capsys):
    target.fizzbuzz_run(5)
    s, _ = capsys.readouterr()
    assert s == "1\n2\nFizz\n4\nBuzz\n"

def test_1から100まで実行する(capsys):
    target.fizzbuzz_run(100)
    s, _ = capsys.readouterr()
    assert 101 == len(s.split("\n"))

def test_プリントする_15まで2(capsys):
    target.fizzbuzz_run2(15)
    s, _ = capsys.readouterr()
    assert s == "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n"

def test_1から100まで実行する2(capsys):
    target.fizzbuzz_run2(100)
    s, _ = capsys.readouterr()
    assert 101 == len(s.split("\n"))
