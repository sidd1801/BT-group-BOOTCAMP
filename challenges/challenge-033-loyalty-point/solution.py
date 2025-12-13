def calculate_loyalty_points(final_total):
    """
    Returns loyalty points based on final payable amount.
    1 point for every ₹100.
    """
    return int(final_total // 100)
