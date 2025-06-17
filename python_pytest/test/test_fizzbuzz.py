import pytest


def fizzbuzz(n):
    return str(n)


def test_1のときは1():
    assert '1' == fizzbuzz(1)


def test_2のときは2():
    assert '2' == fizzbuzz(2)


@pytest.mark.parametrize(
    'expected, num',
    [
        ('1', 1),
        ('2', 2),
        ('Fizz', 3),
    ]
)
def test_fizzbuzz(expected, num):
    assert expected == fizzbuzz(num)



