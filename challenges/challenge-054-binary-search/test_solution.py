# test_solution.py

import solution

def test_binary_search_found():
    assert solution.binary_search([1, 3, 5, 7, 9], 5) is True

def test_binary_search_not_found():
    assert solution.binary_search([1, 3, 5, 7, 9], 4) is False

def test_binary_search_single_element():
    assert solution.binary_search([10], 10) is True

def test_binary_search_empty():
    assert solution.binary_search([], 5) is False

def test_binary_search_first_element():
    assert solution.binary_search([2, 4, 6, 8], 2) is True

def test_binary_search_last_element():
    assert solution.binary_search([2, 4, 6, 8], 8) is True
