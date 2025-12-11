# test_solution.py
import solution

def test_simple_interest_case1():
    assert solution.calculate_simple_interest(1000, 5, 2) == 100

def test_simple_interest_case2():
    assert solution.calculate_simple_interest(1500, 4.5, 3) == 202.5

def test_simple_interest_case3():
    assert solution.calculate_simple_interest(2000, 7, 1) == 140

def test_simple_interest_zero():
    assert solution.calculate_simple_interest(0, 5, 2) == 0

def test_simple_interest_float():
    assert round(solution.calculate_simple_interest(1234.56, 6.5, 1.25), 2) == 100.31

