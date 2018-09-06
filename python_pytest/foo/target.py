def fizzbuzz(i):
    if i % 3 == i % 5 == 0:
        return "FizzBuzz"
    if i % 3 == 0:
        return "Fizz"
    if i % 5 == 0:
        return "Buzz"
    return str(i)


def fizzbuzz_run(count):
    for i in range(count):
        print(fizzbuzz(i + 1))





















def fizzbuzz_run2(count):
    for s in [("Fizz" if i % 3 == 0 else "") +
              ("Buzz" if i % 5 == 0 else "") or
              str(i)
              for i in range(1, count + 1)]:
        print(s)
