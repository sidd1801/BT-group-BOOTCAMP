# test_solution.py

import solution

def test_discount_basic():
    d, final = solution.calculate_discount(1000, 10)
    assert d == 100
    assert final == 900


def test_discount_zero():
    d, final = solution.calculate_discount(500, 0)
    assert d == 0
    assert final == 500


def test_discount_full():
    d, final = solution.calculate_discount(250, 100)
    assert d == 250
    assert final == 0


def test_discount_float():
    d, final = solution.calculate_discount(999.99, 12.5)
    assert round(d, 2) == 125.00
    assert round(final, 2) == 874.99




def test_discount_large_amount():
    d, final = solution.calculate_discount(100000, 7.75)
    assert round(d, 2) == 7750.00
    assert round(final, 2) == 92250.00
