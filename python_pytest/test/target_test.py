from foo import target

def test_func_42():
    assert target.func_42() == 42

def dividable(n):
    return lambda i: i % n == 0

def fizzbuzz(n):
    d3 = dividable(3)
    d5 = dividable(5)
    return [("Fizz" if d3(i) else "") + ("Buzz" if d5(i) else "") or str(i) for i in range(1, n + 1)]

def test_fizzbuzz():
    actual = fizzbuzz(100)
    assert len(actual) == 100
    assert actual[1 - 1] == "1"
    assert actual[3 - 1] == "Fizz"
    assert actual[5 - 1] == "Buzz"
    assert actual[15 - 1] == "FizzBuzz"
    assert actual[99 - 1] == "Fizz"
    assert actual[100 - 1] == "Buzz"

