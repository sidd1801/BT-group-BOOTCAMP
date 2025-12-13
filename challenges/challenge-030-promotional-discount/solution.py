def apply_promotional_discount(item_code, item_total):
    """
    Apply 10% discount if item code is PROMO10.
    Returns (new_item_total, promo_discount_amount)
    """
    item_code = item_code.upper()

    if item_code == "PROMO10":
        discount = item_total * 0.10
        item_total -= discount
        return item_total, discount

    return item_total, 0
