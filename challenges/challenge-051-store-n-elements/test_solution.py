# test_solution.py

import solution

def test_store_elements_basic():
    assert solution.store_elements(3, [10, 20, 30]) == [10, 20, 30]

def test_store_elements_strings():
    assert solution.store_elements(4, ["a", "b", "c", "d"]) == ["a", "b", "c", "d"]

def test_store_elements_mismatch():
    try:
        solution.store_elements(3, [1, 2])  # fewer elements
        assert False
    except ValueError:
        assert True
