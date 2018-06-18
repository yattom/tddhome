# coding: utf-8
import pytest

from foo.magic import Matrix, permutation

@pytest.fixture
def matrix3():
    matrix = Matrix(3)
    matrix.values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return matrix

def test_matrix():
    matrix = Matrix(1)
    assert 1 == matrix.size

def test_matrix_total_of_row(matrix3):
    assert 1 + 2 + 3 == matrix3.row_total(0)
    assert 4 + 5 + 6 == matrix3.row_total(1)
    assert 7 + 8 + 9 == matrix3.row_total(2)

def test_matrix_total_of_column(matrix3):
    assert 1 + 4 + 7 == matrix3.column_total(0)
    assert 2 + 5 + 8 == matrix3.column_total(1)
    assert 3 + 6 + 9 == matrix3.column_total(2)

def test_matrix_total_of_diag(matrix3):
    assert 1 + 5 + 9 == matrix3.diag_down_total()
    assert 3 + 5 + 7 == matrix3.diag_up_total()

def test_matrix_is_magic():
    matrix = Matrix(3)
    matrix.values = [1] * 9
    assert matrix.is_magic()

def test_matrix_is_not_magic(matrix3):
    assert not matrix3.is_magic()

def test_permutation_only_2():
    assert set([(1, 2), (2, 1)]) == set(permutation([1, 2]))

def test_permutation_only_3():
    assert set([(1, 2, 3),
                (1, 3, 2),
                (2, 1, 3),
                (2, 3, 1),
                (3, 1, 2),
                (3, 2, 1)]) == set(permutation([1, 2, 3]))

def test_magic_matrix_3():
    matrix = Matrix(3)
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for p in permutation(values):
        matrix.values = p
        if matrix.is_magic():
            print(p)
