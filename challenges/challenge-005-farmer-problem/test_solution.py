# test_solution.py

import solution


def test_overall_sales():
    result = solution.calculate_overall_sales()
    assert result == 14972800  # Expected exact revenue


def test_chemical_free_sales():
    result = solution.calculate_chemical_free_sales_upto_11_months()
    assert result == 12092800  # Expected chemical-free revenue


def test_difference_sales():
    total = solution.calculate_overall_sales()
    chem_free = solution.calculate_chemical_free_sales_upto_11_months()
    assert total - chem_free == 2880000  # Sugarcane revenue


def test_values_are_positive():
    assert solution.calculate_overall_sales() > 0
    assert solution.calculate_chemical_free_sales_upto_11_months() > 0


def test_chemical_free_less_than_total():
    assert solution.calculate_chemical_free_sales_upto_11_months() < solution.calculate_overall_sales()
