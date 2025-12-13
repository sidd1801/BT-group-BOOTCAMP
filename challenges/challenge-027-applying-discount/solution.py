# solution.py

def calculate_item_total(qty, price):
    return qty * price


def apply_discounts(grand_total, total_quantity):
    discount_1 = 0
    discount_2 = 0

    if grand_total > 10000:       # Rule 1
        discount_1 = grand_total * 0.10
        grand_total -= discount_1

    if total_quantity > 20:       # Rule 2
        discount_2 = grand_total * 0.05
        grand_total -= discount_2

    return grand_total, discount_1, discount_2


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

    final_total, disc1, disc2 = apply_discounts(grand_total, total_quantity)

    print("\n--- DISCOUNT SUMMARY ---")
    print("Original Grand Total:", grand_total)
    print("10% Discount (if applicable):", disc1)
    print("5% Quantity Discount (if applicable):", disc2)
    print("Final Total After Discounts:", final_total)

    return final_total
