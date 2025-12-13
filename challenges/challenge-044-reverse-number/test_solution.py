# test_solution.py

import solution

def test_reverse_positive():
    assert solution.reverse_number(1234) == 4321

def test_reverse_with_zero():
    assert solution.reverse_number(1200) == 21  # Leading zeros disappear

def test_reverse_single_digit():
    assert solution.reverse_number(7) == 7

def test_reverse_negative():
    # Reverse absolute part, then apply negative sign
    assert solution.reverse_number(-123) == -321
