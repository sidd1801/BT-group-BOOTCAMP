import solution

def test_points_exact():
    assert solution.calculate_loyalty_points(500) == 5

def test_points_round_down():
    # 549 → 5 points, not 6
    assert solution.calculate_loyalty_points(549) == 5

def test_no_points():
    assert solution.calculate_loyalty_points(99) == 0

def test_large_points():
    assert solution.calculate_loyalty_points(12345) == 123
