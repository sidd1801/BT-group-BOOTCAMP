# test_solution.py

import solution

def test_sort_ascending():
    assert solution.sort_array([5, 2, 9, 1], "asc") == [1, 2, 5, 9]

def test_sort_descending():
    assert solution.sort_array([5, 2, 9, 1], "desc") == [9, 5, 2, 1]

def test_sort_strings():
    assert solution.sort_array(["c", "a", "b"], "asc") == ["a", "b", "c"]

def test_sort_invalid_order():
    try:
        solution.sort_array([1, 2, 3], "invalid")
        assert False
    except ValueError:
        assert True
