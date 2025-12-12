# test_solution.py

import solution

def test_regular_leap_year():
    assert solution.is_leap_year(2024) is True  # divisible by 4

def test_century_not_leap():
    assert solution.is_leap_year(1900) is False  # divisible by 100 but not 400

def test_century_leap():
    assert solution.is_leap_year(2000) is True  # divisible by 400

def test_non_leap_year():
    assert solution.is_leap_year(2023) is False

def test_edge_case_zero():
    # Year 0 follows divisibility rules → divisible by 400
    assert solution.is_leap_year(0) is True
