# test_solution.py

import solution

def test_square_pattern_1():
    assert solution.perfect_square_pattern(1) == [
        [1]
    ]

def test_square_pattern_2():
    assert solution.perfect_square_pattern(2) == [
        [1],
        [-4, 9]
    ]

def test_square_pattern_3():
    assert solution.perfect_square_pattern(3) == [
        [1],
        [-4, 9],
        [-16, 25, -36]
    ]

def test_square_pattern_4():
    assert solution.perfect_square_pattern(4) == [
        [1],
        [-4, 9],
        [-16, 25, -36],
        [49, -64, 81, -100]
    ]
