# test_solution.py

import solution

def test_min_basic():
    assert solution.min_of_array([5, 3, 8, 2, 9]) == 2

def test_min_negative():
    assert solution.min_of_array([-10, -3, -50, 2]) == -50

def test_min_single():
    assert solution.min_of_array([7]) == 7

def test_min_empty():
    try:
        solution.min_of_array([])
        assert False  # should not reach here
    except ValueError:
        assert True
