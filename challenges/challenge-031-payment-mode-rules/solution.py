def apply_payment_surcharge(total, payment_method):
    """
    Adds surcharge based on payment method.
    Credit Card → 2% surcharge
    Cash → no surcharge
    Returns (total_after_surcharge, surcharge_amount)
    """

    payment_method = payment_method.lower()
    surcharge = 0

    if payment_method == "credit":
        surcharge = total * 0.02
        total += surcharge

    return total, surcharge
