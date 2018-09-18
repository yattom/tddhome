from foo.fizzbuzz import *
import pytest

@pytest.fixture
def fizzbuzz():
    return FizzBuzz()

def test_数1をそのまま(fizzbuzz):
    assert fizzbuzz.translate(1) == "1"

def test_数2をそのまま(fizzbuzz):
    assert fizzbuzz.translate(2) == "2"

@pytest.mark.parametrize('num', [3, 6, 99])
def test_3の倍数はFizzにする(num, fizzbuzz):
    assert fizzbuzz.translate(num) == "Fizz"

def test_5のときはBuzzにする(fizzbuzz):
    assert fizzbuzz.translate(5) == "Buzz"

def test_3と5両方の倍数の場合にはFizzBuzzにする(fizzbuzz):
    assert fizzbuzz.translate(15) == "FizzBuzz"

def test_プリントする(fizzbuzz, capsys):
    print_fizzbuzz(fizzbuzz, 1)
    actual, _ = capsys.readouterr()
    assert actual == "1\n"

def test_1から100までプリントする(fizzbuzz, capsys):
    fizzbuzz.run(100)
    out, _ = capsys.readouterr()
    lines = out.split('\n')
    actual = len(lines)
    assert 100 + 1 == actual
    assert lines[0] == '1'
    assert lines[99] == 'Buzz'

