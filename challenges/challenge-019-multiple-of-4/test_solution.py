# test_solution.py

import solution

def test_basic():
    assert solution.generate_even_squares(70) == [4, 16, 36, 64]

def test_small():
    assert solution.generate_even_squares(10) == [4]

def test_exact_match():
    assert solution.generate_even_squares(36) == [4, 16, 36]

def test_zero():
    assert solution.generate_even_squares(0) == []
