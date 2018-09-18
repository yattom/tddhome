def fizzbuzz(num):
    if num % 15 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return str(num)

def print_fizbuzz(num):
    for i in range(1, num + 1):
        print(fizzbuzz(i))

