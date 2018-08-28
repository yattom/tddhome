from foo.hello import *

SMALLEST_PRIME = 2


def test_hello():
    pass

def is_dividable(target, prime):
    return target % prime == 0

def get_smallest_prime_factor(target):
    prime = SMALLEST_PRIME
    while prime <= target:
        if is_dividable(target, prime):
            target = int(target / prime)
            return prime, target
            break
        prime += 1


def prime_factoring(target):
    prime_factors = []
    while target > 1:
        prime, target = get_smallest_prime_factor(target)
        prime_factors.append(prime)
    return prime_factors

def test_素因数分解():
    assert prime_factoring(100) == [2, 2, 5, 5]
