class FizzBuzz:
    def translate(self, i):
        if i % 15 == 0:
            return "FizzBuzz"
        if i % 3 == 0:
            return "Fizz"
        if i % 5 == 0:
            return "Buzz"
        return str(i)

    def run(self, last):
        for i in range(1, last + 1):
            print(self.translate(i))

def print_fizzbuzz(fizzbuzz, i):
    print(fizzbuzz.translate(i))

