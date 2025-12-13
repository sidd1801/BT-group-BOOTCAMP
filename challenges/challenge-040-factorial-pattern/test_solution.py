# test_solution.py

import solution

def test_factorial_pattern_1():
    assert solution.factorial_pattern(1) == [
        [1]
    ]

def test_factorial_pattern_2():
    assert solution.factorial_pattern(2) == [
        [1],
        [2, 6]
    ]

def test_factorial_pattern_3():
    assert solution.factorial_pattern(3) == [
        [1],
        [2, 6],
        [24, 120, 720]
    ]
