# test_solution.py

import solution

def test_basic_series():
    assert solution.generate_odd_series(10) == [1, 3, 5, 7, 9]

def test_small():
    assert solution.generate_odd_series(1) == [1]

def test_zero():
    assert solution.generate_odd_series(0) == []

def test_limit_not_included():
    assert solution.generate_odd_series(9) == [1, 3, 5, 7, 9]
