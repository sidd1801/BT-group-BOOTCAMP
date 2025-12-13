# solution.py

def calculate_item_total(code, description, quantity, price):
    total = quantity * price
    return {
        "code": code,
        "description": description,
        "quantity": quantity,
        "price": price,
        "total": total
    }


if __name__ == "__main__":
    code = input("Enter item code: ")
    desc = input("Enter item description: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    item = calculate_item_total(code, desc, qty, price)

    print("\n--- ITEM TOTAL ---")
    print("Item Code:", item["code"])
    print("Description:", item["description"])
    print("Quantity:", item["quantity"])
    print("Price:", item["price"])
    print("Total Cost:", item["total"])
