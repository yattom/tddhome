# coding: utf-8
from functools import reduce

class Matrix:
    def __init__(self, size):
        self.size = size

    def row_total(self, row):
        return sum(self.values[row * self.size + i] for i in range(self.size))

    def column_total(self, row):
        return sum(self.values[i * self.size + row] for i in range(self.size))

    def diag_down_total(self):
        return sum(self.values[(self.size - i - 1) + self.size * i] for i in range(self.size))

    def diag_up_total(self):
        return sum(self.values[i + self.size * (self.size - i - 1)] for i in range(self.size))

    def is_magic(self):
        totals = ([self.row_total(r) for r in range(self.size)] +
                  [self.column_total(r) for r in range(self.size)] +
                  [self.diag_down_total(), self.diag_up_total()])
        return reduce(lambda a, b: a and b == totals[0], totals)


def permutation(elements):
    result = [()]
    for e in elements:
        new_result = []
        for base in result:
            for i in range(len(base) + 1):
                combined = tuple(list(base)[:i] + [e] + list(base)[i:])
                new_result.append(combined)
        result = new_result
    return result


