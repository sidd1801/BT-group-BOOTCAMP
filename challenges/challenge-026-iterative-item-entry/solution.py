# solution.py

def calculate_item_total(code, description, quantity, price):
    return quantity * price


def generate_bill():
    grand_total = 0

    while True:
        code = input("Enter item code: ")
        desc = input("Enter item description: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        item_total = calculate_item_total(code, desc, qty, price)
        grand_total += item_total

        print(f"Item Total: ₹{item_total}")

        more = input("Add more items? (y/n): ").lower()
        if more != 'y':
            break

    return grand_total


if __name__ == "__main__":
    total = generate_bill()
    print("\n--- FINAL BILL ---")
    print("Grand Total: ₹", total)
