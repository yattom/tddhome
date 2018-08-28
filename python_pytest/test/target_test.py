from foo.hello import *

def test_hello():
    pass

def prime_factoring(n):
    prime_factors = []
    while n > 1:
        i = 2
        while i <= n:
            if n % i == 0:
                prime_factors.append(i)
                n = int(n / i)
                break
            i += 1
    return prime_factors

def test_素因数分解():
    assert prime_factoring(100) == [2, 2, 5, 5]
