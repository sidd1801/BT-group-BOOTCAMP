# test_solution.py

import solution

def test_num_inc_3():
    assert solution.number_increasing_seq(3) == [
        "1",
        "12",
        "123"
    ]

def test_num_inc_5():
    assert solution.number_increasing_seq(5) == [
        "1",
        "12",
        "123",
        "1234",
        "12345"
    ]

def test_num_inc_1():
    assert solution.number_increasing_seq(1) == ["1"]
