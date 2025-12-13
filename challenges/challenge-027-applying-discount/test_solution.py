# test_solution.py

import solution

def test_rule1_discount():
    final, d1, d2 = solution.apply_discounts(15000, 10)
    assert round(final, 2) == 13500.00    # 10% discount only
    assert round(d1, 2) == 1500.00
    assert d2 == 0

def test_rule2_discount():
    final, d1, d2 = solution.apply_discounts(8000, 25)
    assert round(final, 2) == 7600.00     # 5% discount only
    assert d1 == 0
    assert round(d2, 2) == 400.00

def test_both_discounts():
    final, d1, d2 = solution.apply_discounts(20000, 30)
    # Step 1: 20000 - 10% => 18000
    # Step 2: 18000 - 5% => 17100
    assert round(final, 2) == 17100.00
    assert round(d1, 2) == 2000.00
    assert round(d2, 2) == 900.00
