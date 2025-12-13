# test_solution.py

import solution

def test_even_odd_basic():
    assert solution.count_even_odd([1, 2, 3, 4, 5]) == (2, 3)

def test_even_odd_all_even():
    assert solution.count_even_odd([2, 4, 6, 8]) == (4, 0)

def test_even_odd_all_odd():
    assert solution.count_even_odd([1, 3, 5, 7]) == (0, 4)

def test_even_odd_empty():
    assert solution.count_even_odd([]) == (0, 0)
