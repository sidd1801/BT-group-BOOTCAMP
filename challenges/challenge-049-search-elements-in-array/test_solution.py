# test_solution.py

import solution

def test_search_found():
    assert solution.search_element([10, 20, 30, 40], 30) == True

def test_search_not_found():
    assert solution.search_element([5, 6, 7], 10) == False

def test_search_strings():
    assert solution.search_element(["apple", "banana", "cherry"], "banana") == True

def test_search_empty_array():
    assert solution.search_element([], 5) == False
