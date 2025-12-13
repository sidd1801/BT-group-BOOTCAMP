# test_solution.py

import solution

def test_number_to_words():
    assert solution.number_to_words(270176) == "Two Seven Zero One Seven Six"

def test_small_number():
    assert solution.number_to_words(109) == "One Zero Nine"

def test_single_digit():
    assert solution.number_to_words(5) == "Five"
