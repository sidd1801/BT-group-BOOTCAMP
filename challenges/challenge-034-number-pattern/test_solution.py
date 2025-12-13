# test_solution.py

import solution

def test_pattern_3():
    assert solution.number_pattern_seq(3) == [
        "123",
        "123",
        "123"
    ]

def test_pattern_5():
    assert solution.number_pattern_seq(5) == [
        "12345",
        "12345",
        "12345",
        "12345",
        "12345"
    ]

def test_pattern_1():
    assert solution.number_pattern_seq(1) == ["1"]
