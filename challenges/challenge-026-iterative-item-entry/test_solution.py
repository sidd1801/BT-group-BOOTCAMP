# test_solution.py

import solution

def test_single_item():
    assert solution.calculate_item_total("A1", "Pen", 2, 10) == 20

def test_multiple_items_sum():
    # simulate multiple items
    total1 = solution.calculate_item_total("A1", "Pen", 2, 10)  # 20
    total2 = solution.calculate_item_total("B1", "Book", 1, 100) # 100
    total3 = solution.calculate_item_total("C1", "Bag", 1, 500)  # 500

    assert total1 + total2 + total3 == 620

def test_zero_quantity():
    assert solution.calculate_item_total("X", "Test", 0, 100) == 0
