# test_solution.py

import solution

def test_basic():
    assert solution.generate_series(25) == [1, 1, 2, 3, 5, 8, 13, 21]

def test_exact():
    assert solution.generate_series(21) == [1, 1, 2, 3, 5, 8, 13, 21]

def test_small():
    assert solution.generate_series(2) == [1, 1, 2]

def test_zero():
    assert solution.generate_series(0) == []
