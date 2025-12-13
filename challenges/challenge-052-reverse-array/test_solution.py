# test_solution.py

import solution

def test_reverse_array_basic():
    assert solution.reverse_array([1, 2, 3, 4]) == [4, 3, 2, 1]

def test_reverse_array_strings():
    assert solution.reverse_array(["a", "b", "c"]) == ["c", "b", "a"]

def test_reverse_array_single():
    assert solution.reverse_array([10]) == [10]

def test_reverse_array_empty():
    assert solution.reverse_array([]) == []
