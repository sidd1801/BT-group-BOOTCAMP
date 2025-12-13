# test_solution.py

import solution

def test_split_positive():
    whole, frac = solution.split_number(45.67)
    assert whole == 45
    assert round(frac, 2) == 0.67

def test_split_negative():
    whole, frac = solution.split_number(-12.34)
    assert whole == -12
    assert round(frac, 2) == -0.34

def test_split_integer():
    whole, frac = solution.split_number(100.0)
    assert whole == 100
    assert frac == 0.0
