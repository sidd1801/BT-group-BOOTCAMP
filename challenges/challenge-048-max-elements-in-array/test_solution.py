# test_solution.py

import solution

def test_max_basic():
    assert solution.max_of_array([5, 3, 8, 2, 9]) == 9

def test_max_negative():
    assert solution.max_of_array([-10, -3, -50, -2]) == -2

def test_max_single():
    assert solution.max_of_array([7]) == 7

def test_max_empty():
    try:
        solution.max_of_array([])
        assert False  # should not reach here
    except ValueError:
        assert True
