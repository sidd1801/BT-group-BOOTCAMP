# test_solution.py

import solution

def test_gross_monthly_salary():
    r = solution.calculate_salary(30000, 10000, 10)
    assert r["gross_monthly_salary"] == 40000  # 30k + 10k

def test_annual_gross_salary():
    r = solution.calculate_salary(50000, 20000, 10)
    gross_monthly = 70000
    annual_without_bonus = gross_monthly * 12  # 8,40,000
    expected_bonus = annual_without_bonus * 0.10
    expected_annual = annual_without_bonus + expected_bonus

    assert r["annual_gross_salary"] == expected_annual

def test_zero_bonus():
    r = solution.calculate_salary(40000, 5000, 0)
    expected = (40000 + 5000) * 12
    assert r["annual_gross_salary"] == expected

def test_bonus_amount():
    r = solution.calculate_salary(20000, 5000, 20)
    gross_monthly = 25000
    annual = gross_monthly * 12
    expected_bonus = annual * 0.20
    assert r["bonus_amount"] == expected_bonus
