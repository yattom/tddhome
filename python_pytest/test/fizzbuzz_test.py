def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

def test_数をそのまま文字列に変換する_1の場合():
    assert fizzbuzz(1) == "1"

def test_数をそのまま文字列に変換する_2の場合():
    assert fizzbuzz(2)== "2"

class Test3の倍数のときはFizzに変換する:
    def test_3の場合(self):
        assert fizzbuzz(3) == "Fizz"

class Test5の倍数のときはBuzzに変換する:
    def test_5の場合(self):
        assert fizzbuzz(5) == "Buzz"

class Test3と5の倍数のときはFizzBuzzに変換する:
    def test_15の場合(self):
        assert fizzbuzz(15) == "FizzBuzz"

