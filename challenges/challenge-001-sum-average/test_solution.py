import pytest
from solution import sum_and_average

def test_positive_integers():
    s, avg = sum_and_average(4, 6)
    assert s == 10
    assert avg == 5

def test_negative_numbers():
    s, avg = sum_and_average(-3, -7)
    assert s == -10
    assert avg == -5

def test_mixed_signs():
    s, avg = sum_and_average(10, -4)
    assert s == 6
    assert avg == 3

def test_floats():
    s, avg = sum_and_average(2.5, 1.5)
    assert s == pytest.approx(4.0)
    assert avg == pytest.approx(2.0)

def test_zero_edgecase():
    s, avg = sum_and_average(0, 0)
    assert s == 0
    assert avg == 0

def test_large_values():
    s, avg = sum_and_average(10**18, 10**18)
    assert s == 2 * 10**18
    assert avg == 10**18
