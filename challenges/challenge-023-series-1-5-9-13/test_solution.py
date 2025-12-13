# test_solution.py

import solution

def test_basic():
    assert solution.generate_series(50) == [1, 5, 9, 13, 21, 25, 29, 33, 41, 45]

def test_small():
    assert solution.generate_series(15) == [1, 5, 9, 13]

def test_exact():
    assert solution.generate_series(41) == [1, 5, 9, 13, 21, 25, 29, 33, 41]

def test_zero():
    assert solution.generate_series(0) == []
