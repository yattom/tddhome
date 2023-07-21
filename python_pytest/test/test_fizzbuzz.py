def fizzbuzz_one(num):
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return str(num)


def fizzbuzz_all():
    result = []
    for i in range(100):
        result.append(fizzbuzz_one(i + 1))
    return result


class Test数字をそのまま:
    def test_1の場合(self):
        assert "1" == fizzbuzz_one(1)


class Test3の倍数ならFizz:
    def test_3の場合(self):
        assert "Fizz" == fizzbuzz_one(3)


class Test5の倍数ならBuzz:
    def test_5の場合(self):
        assert "Buzz" == fizzbuzz_one(5)


class Test1から100まで繰り返す:
    def test_結果が100件ある(self):
        result = fizzbuzz_all()
        assert len(result) == 100

    def test_最初が1(self):
        result = fizzbuzz_all()
        assert result[0] == "1"

    def test_最後がBuzz(self):
        result = fizzbuzz_all()
        assert result[99] == "Buzz"

