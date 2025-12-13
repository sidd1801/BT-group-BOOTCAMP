# test_solution.py

import solution

def test_create_matrix_basic():
    result = solution.create_matrix(2, 2, [1, 2, 3, 4])
    assert result == [[1, 2], [3, 4]]

def test_create_matrix_rectangular():
    result = solution.create_matrix(2, 3, [1, 2, 3, 4, 5, 6])
    assert result == [[1, 2, 3], [4, 5, 6]]

def test_transpose_square():
    matrix = [[1, 2], [3, 4]]
    assert solution.transpose_matrix(matrix) == [[1, 3], [2, 4]]

def test_transpose_rectangular():
    matrix = [[1, 2, 3], [4, 5, 6]]
    assert solution.transpose_matrix(matrix) == [[1, 4], [2, 5], [3, 6]]

def test_transpose_empty():
    assert solution.transpose_matrix([]) == []
