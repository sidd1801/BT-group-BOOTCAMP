# test_solution.py

import solution

def test_largest_basic():
    assert solution.largest_of_three(10, 20, 5) == 20

def test_largest_second():
    assert solution.largest_of_three(5, 50, 10) == 50

def test_largest_third():
    assert solution.largest_of_three(3, 7, 9) == 9

def test_all_equal():
    assert solution.largest_of_three(8, 8, 8) == 8

def test_negative_numbers():
    assert solution.largest_of_three(-5, -2, -9) == -2

def test_mixed_numbers():
    assert solution.largest_of_three(-10, 0, 5) == 5
