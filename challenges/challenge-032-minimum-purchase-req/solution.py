def check_minimum_purchase(final_total):
    """
    Ensures minimum purchase of ₹500.
    Returns (allowed, message)
    """
    if final_total < 500:
        return False, "Minimum purchase amount of ₹500 not met."
    return True, "Purchase amount is valid."
