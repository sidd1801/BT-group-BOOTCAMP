# solution.py

def calculate_item_total(qty, price):
    return qty * price


def apply_discounts(grand_total, total_quantity):
    discount_1 = 0
    discount_2 = 0

    if grand_total > 10000:
        discount_1 = grand_total * 0.10
        grand_total -= discount_1

    if total_quantity > 20:
        discount_2 = grand_total * 0.05
        grand_total -= discount_2

    return grand_total, discount_1, discount_2


def apply_membership_discount(total, is_member):
    """
    Apply 2% discount after all other discounts.
    """
    member_discount = 0

    if is_member == 'y':
        member_discount = total * 0.02
        total -= member_discount

    return total, member_discount

def generate_bill():
    grand_total = 0
    total_quantity = 0

    while True:
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        item_total = calculate_item_total(qty, price)
        grand_total += item_total
        total_quantity += qty

        print(f"Item Total: ₹{item_total}")

        more = input("Add more items? (y/n): ").lower()
        if more != 'y':
            break

    # Discount Rules (27)
    discounted_total, d1, d2 = apply_discounts(grand_total, total_quantity)

    # Membership Discount (28)
    member = input("Is the customer a member? (y/n): ").lower()
    final_total, member_disc = apply_membership_discount(discounted_total, member)

    print("\n--- FINAL BILL ---")
    print("Original Grand Total:", grand_total)
    print("10% Discount:", d1)
    print("5% Quantity Discount:", d2)
    print("Membership Discount (2%):", member_disc)
    print("Total Payable:", final_total)

    return final_total
