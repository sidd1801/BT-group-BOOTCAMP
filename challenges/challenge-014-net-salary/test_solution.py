# test_solution.py

import solution

def test_basic_net_salary():
    r = solution.net_salary(600000, 50000)
    assert r["annual_net_salary"] == 550000

def test_zero_tax():
    r = solution.net_salary(400000, 0)
    assert r["annual_net_salary"] == 400000

def test_high_tax():
    r = solution.net_salary(1500000, 156000)
    assert r["annual_net_salary"] == 1344000

def test_equal_tax_and_salary():
    r = solution.net_salary(50000, 50000)
    assert r["annual_net_salary"] == 0
