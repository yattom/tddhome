def work(num):
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return num

def count_up():
    data = []
    for i in range(1,101):
        data.append(work(i))
    return data