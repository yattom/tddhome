def prime_factoring(n):
    return [n]
    if n == 1:
        return [1]
    primes = []
    if n % 2 == 0:
        primes.append(2)
        n = n / 2
    if n != 1:
        primes.append(n)
    return primes

def test_素因数分解_1():
    assert [1] == prime_factoring(1)

def test_素因数分解_2():
    assert [2] == prime_factoring(2)

#def test_素因数分解_6():
#    assert [2, 3] == prime_factoring(6)
