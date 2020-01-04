from typing import List, Dict
import math
from dataclasses import dataclass

'''
1307. Verbal Arithmetic Puzzle
'''
ALL_NUMBERS = list(range(10))


def permutation(vals: List, size: int):
    count = int(math.factorial(len(vals)) / math.factorial(len(vals) - size))
    for i in range(count):
        v = vals[:]
        result = []
        for j in range(len(vals), len(vals) - size, -1):
            result.append(v.pop(i % j))
            i = i // j
        yield result


class Mapping(dict):
    def __setitem__(self, key: str, value: int):
        if key not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            raise ValueError()
        if type(value) is not int:
            raise ValueError()
        super().__setitem__(key, value)

    @staticmethod
    def generate(col_of_prob, overflow, preceding_mapping={}, left_most_chars=[]):
        mappings = []
        chars = sorted(list(set(col_of_prob.words) - set(preceding_mapping.keys())))
        open_numbers = sorted(list(set(ALL_NUMBERS) - set(preceding_mapping.values())))
        for perm in permutation(open_numbers, len(chars)):
            acceptable = True
            m = preceding_mapping.copy()
            for i, p in enumerate(perm):
                assert chars[i] not in m
                m[chars[i]] = p
            for c in left_most_chars:
                if c in m and m[c] == 0:
                    acceptable = False
            left_side = sum([m[c] for c in col_of_prob.words]) + overflow
            if col_of_prob.result in m.keys():
                if left_side % 10 != m[col_of_prob.result]:
                    acceptable = False
            elif left_side % 10 not in m.values():
                m[col_of_prob.result] = left_side % 10
            else:
                acceptable = False

            if acceptable:
                mappings.append(m)
        return mappings


@dataclass
class ColumnOfProblem:
    words: List[str]
    result: str

    def get_allchars(self):
        chars: List[str] = []
        for c in self.words:
            if c not in chars:
                chars.append(c)
        if self.result not in chars:
            chars.append(result)
        return chars


@dataclass
class Problem:
    words: List[str]
    result: str

    def extract_column(self, col_from_back: int) -> ColumnOfProblem:
        return ColumnOfProblem(
                words = [w[-col_from_back] for w in self.words if col_from_back <= len(w)],
                result = self.result[-col_from_back])

    def get_overflow_at(self, col_from_back: int, mapping: Mapping) -> int:
        overflow = 0
        for col in range(1, col_from_back):
            left_side = sum([mapping[c] for c in self.extract_column(col).words]) + overflow
            overflow = left_side // 10
        return overflow


class Solution:
    def isSolvable(self, words: List[str], result: str, possible_mappings:List[Mapping]=None) -> bool:
        problem = Problem(
                words=[w for w in words],
                result=result)
        mappings: List[Mapping] = [Mapping()]
        if len(result) > max([len(w) for w in words]):
            mappings[0][result[0]] = 1
        left_most_chars = [w[0] for w in words]
        for col in range(1, len(result) + 1):
            col_of_prob = problem.extract_column(col)
            refined_mappings: List[Mapping] = []
            for m in mappings:
                overflow = problem.get_overflow_at(col, m)
                refined_mappings += Mapping.generate(col_of_prob, overflow, m, left_most_chars)
            mappings = refined_mappings

        if mappings:
            if possible_mappings is not None:
                possible_mappings += mappings
            return True
        else:
            return False


import pytest

@pytest.fixture
def sut():
    return Solution()


class TestMapping:
    def test_put_and_get(self):
        sut = Mapping()
        sut['A'] = 0
        assert sut['A'] == 0

    def test_permutation(self):
        actual = list(permutation(['A', 'B', 'C', 'D', 'E'], 2))
        assert len(actual) == 5 * 4
        assert actual[0] == [ 'A', 'B' ]
        assert actual[1] == [ 'B', 'A' ]
        assert actual[2] == [ 'C', 'A' ]
        assert actual[3] == [ 'D', 'A' ]
        assert actual[-1] == [ 'E', 'D' ]

        # assert uniqueness
        assert len(actual) == len(set(["".join(l) for l in actual]))

    class TestGenerate:
        def test_generate_will_return_unique_mappings(self):
            prob = ColumnOfProblem(words=['A', 'B', 'C', 'D', 'E'], result='F')
            mappings = Mapping.generate(prob, 0)
            assert len(mappings) == len(set(["".join([f"{c}{m[c]}" for c in m]) for m in mappings]))

        def test_generate_with_expression_constraint(self):
            prob = ColumnOfProblem(words=['A', 'B'], result='C')
            mappings = Mapping.generate(prob, 0)
            assert len(mappings) == 72
            assert mappings[0] == { 'A': 1, 'B': 2, 'C': 3 }
            assert mappings[1] == { 'A': 2, 'B': 1, 'C': 3 }
            assert mappings[2] == { 'A': 3, 'B': 1, 'C': 4 }
            assert mappings[3] == { 'A': 4, 'B': 1, 'C': 5 }
            assert mappings[-1] == { 'A': 9, 'B': 8, 'C': 7 }

        def test_generate_with_expression_constraint_with_overflow(self):
            prob = ColumnOfProblem(words=['A', 'B'], result='C')
            mappings = Mapping.generate(prob, 1)
            assert len(mappings) == 72
            assert mappings[0] == { 'A': 0, 'B': 1, 'C': 2 }
            assert mappings[1] == { 'A': 1, 'B': 0, 'C': 2 }
            assert mappings[2] == { 'A': 2, 'B': 0, 'C': 3 }
            assert mappings[3] == { 'A': 3, 'B': 0, 'C': 4 }
            assert mappings[-1] == { 'A': 8, 'B': 7, 'C': 6 }

        def test_generate_with_expression_constraint_for_same_char(self):
            prob = ColumnOfProblem(words=['A', 'A'], result='B')
            mappings = Mapping.generate(prob, 0)
            assert len(mappings) == 9
            assert mappings[0] == { 'A': 1, 'B': 2 }
            assert mappings[1] == { 'A': 2, 'B': 4 }
            assert mappings[2] == { 'A': 3, 'B': 6 }
            assert mappings[3] == { 'A': 4, 'B': 8 }
            assert mappings[4] == { 'A': 5, 'B': 0 }
            assert mappings[-1] == { 'A': 9, 'B': 8 }

        def test_generate_with_expression_constraint_for_same_char_in_result(self):
            prob = ColumnOfProblem(words=['A', 'B'], result='B')
            mappings = Mapping.generate(prob, 0)
            assert len(mappings) == 9
            assert mappings[0] == { 'A': 0, 'B': 1 }
            assert mappings[1] == { 'A': 0, 'B': 2 }
            assert mappings[2] == { 'A': 0, 'B': 3 }
            assert mappings[3] == { 'A': 0, 'B': 4 }
            assert mappings[4] == { 'A': 0, 'B': 5 }
            assert mappings[-1] == { 'A': 0, 'B': 9 }

        def test_generate_with_expression_constraint_for_same_char_in_result_2(self):
            prob = ColumnOfProblem(words=['A', 'B'], result='A')
            mappings = Mapping.generate(prob, 1)
            assert len(mappings) == 9
            assert mappings[0] == { 'A': 0, 'B': 9 }
            assert mappings[1] == { 'A': 1, 'B': 9 }
            assert mappings[2] == { 'A': 2, 'B': 9 }
            assert mappings[3] == { 'A': 3, 'B': 9 }
            assert mappings[4] == { 'A': 4, 'B': 9 }
            assert mappings[-1] == { 'A': 8, 'B': 9 }

        def test_generate_with_preceding_mapping(self):
            # AB+BC=DA <- 12+29+41
            prob = Problem(words=['AB', 'BC'], result='DA')
            col_of_prob1 = prob.extract_column(1)
            mappings = Mapping.generate(col_of_prob1, 0)

            col_of_prob2 = prob.extract_column(2)
            refined_mappings = []
            for m in mappings:
                overflow = sum([m[c] for c in col_of_prob1.words]) // 10
                refined_mappings += Mapping.generate(col_of_prob2, overflow, m)

            assert len(refined_mappings) == 60
            assert refined_mappings[0] == { 'A': 3, 'B': 1, 'C': 2, 'D': 4 }
            assert refined_mappings[1] == { 'A': 3, 'B': 2, 'C': 1, 'D': 5 }
            assert refined_mappings[2] == { 'A': 4, 'B': 3, 'C': 1, 'D': 7 }
            assert refined_mappings[3] == { 'A': 5, 'B': 4, 'C': 1, 'D': 9 }
            assert refined_mappings[-1] == { 'A': 7, 'B': 8, 'C': 9, 'D': 6 }

        def test_generate_for_left_most_col(self):
            prob = ColumnOfProblem(words=[], result='X')
            mappings = Mapping.generate(prob, 1)
            assert len(mappings) == 1
            assert mappings[0] == { 'X': 1 }

        def test_generate_for_left_most_col_with_preceding_mapping(self):
            prob = ColumnOfProblem(words=[], result='X')
            prec = Mapping()
            prec['X'] = 5
            mappings = Mapping.generate(prob, 1, prec)
            assert len(mappings) == 0


@pytest.fixture
def problem():
    return Problem(["SEND", "MORE"], "MONEY")


class TestProblem:
    def test_setup(self):
        sut = Problem(["SEND", "MORE"], "MONEY")
        assert sut.words == ["SEND", "MORE"]
        assert sut.result == "MONEY"

    def test_extract_column(self, problem):
        col = problem.extract_column(1)
        assert col.words == ["D", "E"]
        assert col.result == "Y"


@pytest.mark.parametrize("words,result,answer,expected_mappings", [
    (["SEND", "MORE"], "MONEY", True, [{'D': 7, 'E': 5, 'M': 1, 'N': 6, 'O': 0, 'R': 8, 'S': 9, 'Y': 2}]),
    (["SIX","SEVEN","SEVEN"], "TWENTY", True, []),
    (["THIS","IS","TOO"], "FUNNY", True, []),
    (["LEET","CODE"], "POINT", False, []),
])
def test_isSolvable(sut, words, result, answer, expected_mappings):
    mappings = []
    assert sut.isSolvable(words, result, possible_mappings=mappings) == answer
    for m in mappings:
        assert len(m.values()) == len(set(m.values()))
    for i, m in enumerate(expected_mappings):
        assert mappings[i] == m



