# test_solution.py

import solution

def test_star_inc_3():
    assert solution.star_increasing(3) == [
        "*",
        "**",
        "***"
    ]

def test_star_inc_5():
    assert solution.star_increasing(5) == [
        "*",
        "**",
        "***",
        "****",
        "*****"
    ]

def test_star_inc_1():
    assert solution.star_increasing(1) == ["*"]
