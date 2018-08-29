import pytest
from foo.hello import *

def test_hello():
    string = hello()
    assert string == "Hello, World!"

def test_計算機_足し算():
    answer = Calculator().plus(1, 1)
    assert answer == 2

def test_計算機_足し算_計算できない場合():
    answer = Calculator().plus("a", "b")
    assert answer == 0

def test_計算機_引き算():
    answer = Calculator().minus(2, 1)
    assert answer == 1

def test_計算機_引き算_計算できない場合():
    answer = Calculator().minus("a", "b")
    assert answer == 0

@pytest.mark.parametrize("n, e", [
    (1, [1]),  # 1の場合
    (2, [2]),  # 最小の素数
    (4, [2, 2]),  # 2の乗数
    (6, [2, 3]),  # 適当な小さい数
    (100, [2, 2, 5, 5]),  # 適当な大きい数
    ])
def test_素因数分解(n, e):
    assert prime_factoring(n) == e

def test_最小の素因数_最小の素数の場合():
    assert get_smallest_prime(2) == 2

def test_最小の素因数_3の場合():
    assert get_smallest_prime(3) == 3

def test_最小の素因数_3の乗数の場合():
    assert get_smallest_prime(9) == 3

def test_最小の素因数_大きな素数の場合():
    assert get_smallest_prime(103) == 103
