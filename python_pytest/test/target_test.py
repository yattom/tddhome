import pytest
from foo.target import *



class Test3の倍数でFizz():
    def test_3の場合(self):
        assert work(3) == "Fizz"

    def test_18の場合(self):
        assert work(18) == "Fizz"


class Test5の倍数でBuzz():
    def test_5の場合(self):
        assert work(5) == "Buzz"

    def test_20の場合(self):
        assert work(20) == "Buzz"

class Test15の倍数でFizzBuzz():
    def test_15の場合(self):
        assert work(15) == "FizzBuzz"

    def test_30の場合(self):
        assert work(30) == "FizzBuzz"

class Testそれ以外の数():
    def test_1の場合1(self):
        assert work(1) == 1

    def test_2の場合2(self):
        assert work(2) == 2

def test_1から15までの結果():
    assert count_up()[:15] == [1,2,"Fizz",4,"Buzz",
                          "Fizz",7,8,"Fizz","Buzz",
                          11,"Fizz",13,14,"FizzBuzz"]

