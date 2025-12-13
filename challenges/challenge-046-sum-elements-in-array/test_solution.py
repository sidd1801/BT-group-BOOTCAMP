# test_solution.py

import solution

def test_sum_basic():
    assert solution.sum_of_array([1, 2, 3, 4]) == 10

def test_sum_with_negatives():
    assert solution.sum_of_array([-5, 10, -3]) == 2

def test_sum_empty():
    assert solution.sum_of_array([]) == 0

def test_sum_floats():
    assert solution.sum_of_array([1.5, 2.5]) == 4.0
