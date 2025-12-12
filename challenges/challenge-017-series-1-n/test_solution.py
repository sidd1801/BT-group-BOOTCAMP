# test_solution.py

import solution

def test_series_basic():
    assert solution.generate_series(5) == [1, 2, 3, 4, 5]

def test_series_one():
    assert solution.generate_series(1) == [1]

def test_series_zero():
    assert solution.generate_series(0) == []

def test_series_large():
    assert solution.generate_series(10)[-1] == 10
