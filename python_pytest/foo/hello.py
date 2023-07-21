class ClosedRange:
    def __init__(self, lower, upper):
        if lower > upper:
            raise ValueError('下端点が上端点より大きい')
        self.lower = lower
        self.upper = upper

    def include(self, num):
        return self.lower <= num <= self.upper


def hello():
    return "Hello, World!"
