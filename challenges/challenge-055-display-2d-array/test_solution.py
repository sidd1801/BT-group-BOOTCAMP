# test_solution.py

import solution

def test_2d_array_basic():
    result = solution.create_2d_array(2, 2, [1, 2, 3, 4])
    assert result == [[1, 2], [3, 4]]

def test_2d_array_rectangular():
    result = solution.create_2d_array(2, 3, [1, 2, 3, 4, 5, 6])
    assert result == [[1, 2, 3], [4, 5, 6]]

def test_2d_array_single_row():
    result = solution.create_2d_array(1, 3, [7, 8, 9])
    assert result == [[7, 8, 9]]

def test_2d_array_invalid_size():
    try:
        solution.create_2d_array(2, 2, [1, 2, 3])
        assert False
    except ValueError:
        assert True
