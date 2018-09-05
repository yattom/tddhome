import pytest

from foo.target import fizzbuzz

@pytest.mark.parametrize('i,s', [(1, "1")])
def test_数をそのまま文字列にする(i, s):
    assert fizzbuzz(i) == s

@pytest.mark.parametrize('i', [3])
def test_3の倍数はFizzにする(i):
    assert fizzbuzz(i) == "Fizz"

@pytest.mark.parametrize('i', [5])
def test_5の倍数はBuzzにする(i):
    assert fizzbuzz(i) == "Buzz"

@pytest.mark.parametrize('i', [15])
def test_3と5の倍数はFizzBuzzにする(i):
    assert fizzbuzz(i) == "FizzBuzz"

def test_1から100まで():
    assert count == 100

