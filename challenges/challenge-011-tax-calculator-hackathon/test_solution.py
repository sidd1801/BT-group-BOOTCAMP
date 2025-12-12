# test_solution.py
import solution

def test_no_tax():
    r = solution.generate_report("A", 20000)  # 20k monthly => 240k annual => below 3L after deduction
    assert r["tax_payable"] == 0

def test_mid_salary():
    r = solution.generate_report("B", 60000)  # 720k annual → taxable 670k
    assert r["taxable_income"] == 670000

def test_high_salary():
    r = solution.generate_report("C", 150000)  # 18L annual
    assert r["taxable_income"] == 1750000  # 18L - 50k

def test_name_preserved():
    r = solution.generate_report("John", 50000)
    assert r["name"] == "John"
