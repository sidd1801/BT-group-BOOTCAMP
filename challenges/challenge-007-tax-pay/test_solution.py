# test_solution.py

import solution

def test_salary_above_3L():
    assert solution.must_pay_tax(400000) is True

def test_salary_equal_3L():
    assert solution.must_pay_tax(300000) is False

def test_salary_below_3L():
    assert solution.must_pay_tax(250000) is False

def test_salary_zero():
    assert solution.must_pay_tax(0) is False

def test_salary_edge_case():
    assert solution.must_pay_tax(300000.01) is True
