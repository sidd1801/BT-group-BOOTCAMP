# test_solution.py

import solution

def test_matrix_multiply_square():
    A = [[1, 2],
         [3, 4]]

    B = [[5, 6],
         [7, 8]]

    assert solution.multiply_matrices(A, B) == [
        [19, 22],
        [43, 50]
    ]

def test_matrix_multiply_rectangular():
    A = [[1, 2, 3],
         [4, 5, 6]]

    B = [[7, 8],
         [9, 10],
         [11, 12]]

    assert solution.multiply_matrices(A, B) == [
        [58, 64],
        [139, 154]
    ]

def test_matrix_multiply_single_element():
    assert solution.multiply_matrices([[5]], [[4]]) == [[20]]

def test_invalid_dimensions():
    try:
        solution.multiply_matrices([[1, 2]], [[1, 2]])
        assert False
    except ValueError:
        assert True
