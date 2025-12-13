import solution

def test_promo_applied():
    new_total, discount = solution.apply_promotional_discount("PROMO10", 1000)
    assert round(new_total, 2) == 900.00
    assert round(discount, 2) == 100.00

def test_promo_case_insensitive():
    new_total, discount = solution.apply_promotional_discount("promo10", 500)
    assert round(new_total, 2) == 450.00

def test_no_promo():
    new_total, discount = solution.apply_promotional_discount("ABC", 1000)
    assert new_total == 1000
    assert discount == 0
