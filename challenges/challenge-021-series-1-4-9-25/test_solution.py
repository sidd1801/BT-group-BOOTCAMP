# test_solution.py

import solution

def test_basic():
    assert solution.generate_series(90) == [1, 4, 9, 25, 36, 49, 81]

def test_exact_match():
    assert solution.generate_series(81) == [1, 4, 9, 25, 36, 49, 81]

def test_small():
    assert solution.generate_series(10) == [1, 4, 9]

def test_skip_multiples_of_4():
    # should skip 16, 64, 144...
    series = solution.generate_series(200)
    assert 16 not in series and 64 not in series

def test_zero():
    assert solution.generate_series(0) == []
