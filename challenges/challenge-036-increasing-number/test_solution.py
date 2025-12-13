# test_solution.py

import solution

def test_inc_num_3():
    assert solution.number_increasing_repeat(3) == [
        "1",
        "22",
        "333"
    ]

def test_inc_num_5():
    assert solution.number_increasing_repeat(5) == [
        "1",
        "22",
        "333",
        "4444",
        "55555"
    ]

def test_inc_num_1():
    assert solution.number_increasing_repeat(1) == ["1"]
