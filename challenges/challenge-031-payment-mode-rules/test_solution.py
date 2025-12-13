import solution

def test_cash_no_surcharge():
    total, surcharge = solution.apply_payment_surcharge(10000, "cash")
    assert total == 10000
    assert surcharge == 0

def test_credit_surcharge():
    total, surcharge = solution.apply_payment_surcharge(10000, "credit")
    assert round(total, 2) == 10200.00
    assert round(surcharge, 2) == 200.00

def test_case_insensitive():
    total, surcharge = solution.apply_payment_surcharge(20000, "CREDIT")
    assert round(total, 2) == 20400.00
