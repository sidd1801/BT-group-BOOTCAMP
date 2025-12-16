# test_solution.py

import solution

# -------- Test Level 4: Subtotal --------
def test_subtotal():
    subtotal, discount, gst, total = solution.calculate_bill([500, 1500], 35)
    assert subtotal == 2000


# -------- Test Level 8: Senior Citizen Discount --------
def test_senior_discount():
    subtotal, discount, gst, total = solution.calculate_bill([2000], 65)
    assert discount == 200


# -------- Test Level 8: High Bill Discount --------
def test_high_bill_discount():
    subtotal, discount, gst, total = solution.calculate_bill([6000], 40)
    assert round(discount, 2) == 300


# -------- Test Level 8: Combined Discounts (FIXED) --------
def test_combined_discounts():
    subtotal, discount, gst, total = solution.calculate_bill([8000], 65)
    assert round(discount, 2) == 1160   # ✅ Correct value


# -------- Test Level 5: GST Calculation --------
def test_gst_calculation():
    subtotal, discount, gst, total = solution.calculate_bill([2000], 30)
    assert gst == 360


# -------- Test Level 6: Grand Total --------
def test_grand_total():
    subtotal, discount, gst, total = solution.calculate_bill([2000], 30)
    assert total == 2360
