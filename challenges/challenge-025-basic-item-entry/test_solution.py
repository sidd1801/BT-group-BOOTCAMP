# test_solution.py

import solution

def test_basic_total():
    item = solution.calculate_item_total("A1", "Pen", 5, 10)
    assert item["total"] == 50

def test_decimal_price():
    item = solution.calculate_item_total("B2", "Book", 2, 99.5)
    assert item["total"] == 199.0

def test_zero_quantity():
    item = solution.calculate_item_total("C3", "Eraser", 0, 5)
    assert item["total"] == 0
