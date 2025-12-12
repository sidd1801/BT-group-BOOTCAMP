# test_solution.py

import solution

def test_rebate_under_7l():
    r = solution.calculate_tax(600000)
    assert r["total_tax_payable"] == 0

def test_tax_850k():
    r = solution.calculate_tax(850000)
    assert r["tax_before_rebate"] == 40000.00
    assert r["cess"] == 1600.00
    assert r["total_tax_payable"] == 41600.00

def test_tax_15l():
    r = solution.calculate_tax(1500000)
    assert r["tax_before_rebate"] == 150000.00
    assert r["total_tax_payable"] == 156000.00

def test_tax_20l():
    r = solution.calculate_tax(2000000)
    assert r["tax_before_rebate"] == 300000.00
    assert r["total_tax_payable"] == 312000.00
