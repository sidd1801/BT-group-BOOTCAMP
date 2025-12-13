import solution

def test_tax_low_amount():
    tax, total = solution.calculate_tax(3000)
    assert round(tax, 2) == 150.00  # 5%
    assert round(total, 2) == 3150.00

def test_tax_mid_amount():
    tax, total = solution.calculate_tax(10000)
    assert round(tax, 2) == 1000.00  # 10%
    assert round(total, 2) == 11000.00

def test_tax_high_amount():
    tax, total = solution.calculate_tax(30000)
    assert round(tax, 2) == 4500.00  # 15%
    assert round(total, 2) == 34500.00
