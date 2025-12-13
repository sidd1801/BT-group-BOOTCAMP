import solution

def test_minimum_not_met():
    ok, msg = solution.check_minimum_purchase(400)
    assert ok is False
    assert "not met" in msg.lower()

def test_minimum_met():
    ok, msg = solution.check_minimum_purchase(500)
    assert ok is True

def test_above_minimum():
    ok, msg = solution.check_minimum_purchase(2000)
    assert ok is True
