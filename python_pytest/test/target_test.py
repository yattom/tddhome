from foo.target import *
import pytest

class Test数はそのまま:
    def test_数1をそのまま(self):
        assert fizzbuzz(1) == "1"

    def test_数2をそのまま(self):
        assert fizzbuzz(2) == "2"

@pytest.mark.parametrize('num', [3, 6])
def test_ただし3の倍数のときはFizzにする(num):
    assert fizzbuzz(num) == "Fizz"

def test_5の倍数のときはBuzzにする():
    assert fizzbuzz(5) == "Buzz"

def test_3と5両方の倍数の場合にはFizzBuzzにする():
    assert fizzbuzz(15) == "FizzBuzz"

class Test指定した数まで実行する:
    def test_1から5までプリントする(self, capsys):
        print_fizbuzz(5)
        actual, _ = capsys.readouterr()
        assert actual == "1\n2\nFizz\n4\nBuzz\n"

    def test_1から100までプリントする(self, capsys):
        print_fizbuzz(100)
        actual, _ = capsys.readouterr()
        actual = actual.split('\n')
        assert 100 + 1 == len(actual)

