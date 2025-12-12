# test_solution.py

import solution


def test_name_validation():
    assert solution.validate_name("John")[0] is True
    assert solution.validate_name("John123")[0] is False


def test_empid_validation():
    assert solution.validate_empid("E1234")[0] is True
    assert solution.validate_empid("12!@#")[0] is False


def test_basic_salary_validation():
    assert solution.validate_basic_salary("50000")[0] is True
    assert solution.validate_basic_salary("-10")[0] is False


def test_allowance_validation():
    assert solution.validate_allowances("10000")[0] is True
    assert solution.validate_allowances("-5")[0] is False


def test_bonus_validation():
    assert solution.validate_bonus("50")[0] is True
    assert solution.validate_bonus("150")[0] is False


def test_derived_validation():
    ok, _ = solution.validate_derived(50000, 600000)
    assert ok is True
    ok2, _ = solution.validate_derived(0, 100000)
    assert ok2 is False
