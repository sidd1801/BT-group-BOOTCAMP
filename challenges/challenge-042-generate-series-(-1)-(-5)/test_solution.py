# test_solution.py

import solution

def test_series_small():
    assert solution.generate_series(10) == [1, -5, 9]

def test_series_medium():
    assert solution.generate_series(25) == [1, -5, 9, -13, 17, -21]

def test_series_exact_match():
    assert solution.generate_series(21) == [1, -5, 9, -13, 17, -21]

def test_series_limit():
    assert solution.generate_series(1) == [1]
