# test_solution.py

import solution

def test_taxable_income_basic():
    r = solution.calculate_taxable_income(500000)
    assert r["annual_gross_salary"] == 500000
    assert r["standard_deduction"] == 50000
    assert r["taxable_income"] == 450000

def test_small_salary():
    r = solution.calculate_taxable_income(30000)
    # deduction cannot exceed salary
    assert r["standard_deduction"] == 30000
    assert r["taxable_income"] == 0

def test_exact_boundary():
    r = solution.calculate_taxable_income(50000)
    assert r["standard_deduction"] == 50000
    assert r["taxable_income"] == 0

def test_zero_salary():
    r = solution.calculate_taxable_income(0)
    assert r["standard_deduction"] == 0
    assert r["taxable_income"] == 0
