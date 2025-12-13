# test_solution.py

import solution

def test_sum_2d_basic():
    matrix = [
        [1, 2],
        [3, 4]
    ]
    assert solution.sum_2d_array(matrix) == 10

def test_sum_2d_rectangular():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    assert solution.sum_2d_array(matrix) == 21

def test_sum_2d_single_row():
    assert solution.sum_2d_array([[5, 10, 15]]) == 30

def test_sum_2d_empty():
    assert solution.sum_2d_array([]) == 0
