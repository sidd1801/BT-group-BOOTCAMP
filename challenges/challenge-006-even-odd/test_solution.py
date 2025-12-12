# test_solution.py

import solution

def test_even_number():
    assert solution.is_even(10) is True

def test_odd_number():
    assert solution.is_even(7) is False

def test_zero():
    assert solution.is_even(0) is True  # Zero is even

def test_negative_even():
    assert solution.is_even(-8) is True

def test_negative_odd():
    assert solution.is_even(-5) is False
