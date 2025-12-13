# test_solution.py

import solution

def test_star_pattern_3():
    assert solution.star_pattern(3) == ["***", "***", "***"]

def test_star_pattern_5():
    assert solution.star_pattern(5) == ["*****", "*****", "*****", "*****", "*****"]

def test_star_pattern_1():
    assert solution.star_pattern(1) == ["*"]
