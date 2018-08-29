def hello():
    return "Hello, World!"

class Calculator:
    def is_number(self, a, b):
        if not(type(a) == int and type(b) == int):
            return False
        return True

    def plus(self, a, b):
        if not self.is_number(a, b):
            return 0
        return a + b

    def minus(self, a, b):
        if not self.is_number(a, b):
            return 0
        return a - b

def get_smallest_prime(n):
    i = 2
    while True:
        if n % i == 0:
            return i
        i += 1

def prime_factoring(n):
    if n == 1:
        return [1]
    f = []
    while n > 1:
        p = get_smallest_prime(n)
        f.append(p)
        n = n / p
    return f

