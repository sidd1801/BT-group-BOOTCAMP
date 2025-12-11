# test_solution.py

import solution

def test_swap_basic():
    a, b = solution.swap_numbers(10, 20)
    assert a == 20 and b == 10

def test_swap_zero():
    a, b = solution.swap_numbers(0, 5)
    assert a == 5 and b == 0

def test_swap_negative():
    a, b = solution.swap_numbers(-3, 9)
    assert a == 9 and b == -3

def test_swap_same():
    a, b = solution.swap_numbers(7, 7)
    assert a == 7 and b == 7

def test_swap_float():
    a, b = solution.swap_numbers(12.5, 99.75)
    assert a == 99.75 and b == 12.5
