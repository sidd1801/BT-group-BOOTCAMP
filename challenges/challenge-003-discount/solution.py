# solution.py

def calculate_discount(total_amount, discount_percent):
    """
    Calculate the discount value and final price.
    Returns a tuple: (discount_amount, final_price)
    """
    discount_amount = (total_amount * discount_percent) / 100
    final_price = total_amount - discount_amount
    return discount_amount, final_price




if __name__ == "__main__":
    total = float(input("Enter total amount: "))
    discount = float(input("Enter discount percentage: "))

    d_amount, final_amount = calculate_discount(total, discount)

    print("Discount Amount =", d_amount)
    print("Final Price =", final_amount)
