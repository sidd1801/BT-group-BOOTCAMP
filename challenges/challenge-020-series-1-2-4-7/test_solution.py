# test_solution.py

import solution

def test_basic():
    assert solution.generate_series(25) == [1, 2, 4, 7, 11, 16, 22]

def test_small():
    assert solution.generate_series(5) == [1, 2, 4]

def test_exact_match():
    assert solution.generate_series(22) == [1, 2, 4, 7, 11, 16, 22]

def test_zero():
    assert solution.generate_series(0) == []
