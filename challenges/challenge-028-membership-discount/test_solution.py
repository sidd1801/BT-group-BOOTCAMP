import solution

def test_member_discount():
    final, mdisc = solution.apply_membership_discount(10000, 'y')
    assert round(final, 2) == 9800.00
    assert round(mdisc, 2) == 200.00

def test_non_member():
    final, mdisc = solution.apply_membership_discount(10000, 'n')
    assert final == 10000
    assert mdisc == 0

def test_combined_membership_after_discounts():
    # Sample: calculation after previous discounts
    # grand_total = 20000 -> after 10% discount = 18000 -> after 5% discount = 17100
    # membership discount = 17100 * 2% = 342
    final, d1, d2 = solution.apply_discounts(20000, 30)
    final2, md = solution.apply_membership_discount(final, 'y')

    assert round(final2, 2) == round(final - (final * 0.02), 2)
    assert round(md, 2) == round(final * 0.02, 2)
