# test_solution.py

import solution


def test_gross_monthly_salary():
    assert solution.gross_monthly_salary(50000, 20000) == 70000


def test_taxable_income():
    assert solution.taxable_income(900000) == 850000


def test_tax_calculation():
    r = solution.tax_breakdown(850000)
    assert r["tax_before_rebate"] == 40000.00
    assert r["total_tax"] == 41600.00


def test_report_values():
    r = solution.generate_report("John", "E123", 50000, 20000)
    assert r["gross_monthly_salary"] == 70000
    assert r["annual_gross_salary"] == 840000
    assert r["taxable_income"] == 790000
