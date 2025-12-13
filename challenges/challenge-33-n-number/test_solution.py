# test_solution.py

import solution

def test_pattern_3():
    assert solution.number_pattern_same(3) == [
        "111",
        "222",
        "333"
    ]

def test_pattern_5():
    assert solution.number_pattern_same(5) == [
        "11111",
        "22222",
        "33333",
        "44444",
        "55555"
    ]

def test_pattern_1():
    assert solution.number_pattern_same(1) == ["1"]
