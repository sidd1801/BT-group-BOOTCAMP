def calculate_tax(total):
    """
    Applies tiered tax based on the total purchase amount.
    Returns (tax_amount, total_after_tax)
    """

    if total < 5000:
        tax = total * 0.05
    elif total <= 20000:
        tax = total * 0.10
    else:
        tax = total * 0.15

    total_after_tax = total + tax
    return tax, total_after_tax
