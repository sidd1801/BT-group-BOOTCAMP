# test_solution.py

import solution

def test_fibonacci_pattern_1():
    assert solution.fibonacci_pattern(1) == [
        [1]
    ]

def test_fibonacci_pattern_2():
    assert solution.fibonacci_pattern(2) == [
        [1],
        [1, 2]
    ]

def test_fibonacci_pattern_4():
    assert solution.fibonacci_pattern(4) == [
        [1],
        [1, 2],
        [3, 5, 8],
        [13, 21, 34, 55]
    ]
