# test_solution.py

import solution

def test_basic():
    assert solution.generate_series(30) == [1, 4, 7, 12, 23]

def test_exact():
    assert solution.generate_series(23) == [1, 4, 7, 12, 23]

def test_small():
    assert solution.generate_series(10) == [1, 4, 7]

def test_zero():
    assert solution.generate_series(0) == []
