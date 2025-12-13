# test_solution.py

import solution

def test_search_2d_found():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    assert solution.search_2d_array(matrix, 5) is True

def test_search_2d_not_found():
    matrix = [
        [1, 2],
        [3, 4]
    ]
    assert solution.search_2d_array(matrix, 10) is False

def test_search_2d_single_element():
    assert solution.search_2d_array([[7]], 7) is True

def test_search_2d_empty():
    assert solution.search_2d_array([], 5) is False
