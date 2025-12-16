# ==============================
# HealWell Care Hospital System
# ==============================

# -------- Level 7: Admin Setup --------
# Services and costs are configurable by admin

def setup_services():
    services = []
    costs = []

    n = int(input("Enter number of services for today: "))
    for i in range(n):
        service = input(f"Enter service {i+1} name: ")
        cost = int(input(f"Enter cost for {service}: "))
        services.append(service)
        costs.append(cost)

    return services, costs


# -------- Level 3, 4, 5, 8: Billing Logic --------
# (This function is testable)

def calculate_bill(selected_costs, age):
    # Level 4: Subtotal
    subtotal = sum(selected_costs)

    # Level 8: Discounts
    discount = 0
    if age >= 60:                      # Senior Citizen Discount
        discount += subtotal * 0.10

    if subtotal > 5000:                # High Bill Discount
        discount += (subtotal - discount) * 0.05

    amount_after_discount = subtotal - discount

    # Level 5: GST
    gst = amount_after_discount * 0.18
    grand_total = amount_after_discount + gst

    return subtotal, discount, gst, grand_total


# -------- Level 1, 2, 6: User Interaction --------
# (Runs only when file is executed directly)

if __name__ == "__main__":

    # Level 7: Admin sets services
    services, costs = setup_services()

    # Level 1: Patient Details
    name = input("\nEnter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    contact = input("Enter Contact Number: ")

    # Level 2: Display Services
    print("\nAvailable Services:")
    for i in range(len(services)):
        print(f"{i+1}. {services[i]} - ₹{costs[i]}")

    choices = input("\nSelect service numbers (comma separated): ")
    choice_list = choices.split(",")

    # Level 3: Fetch Selected Services & Costs
    selected_services = []
    selected_costs = []

    for ch in choice_list:
        idx = int(ch.strip()) - 1
        selected_services.append(services[idx])
        selected_costs.append(costs[idx])

    # Level 4, 5, 8: Bill Calculation
    subtotal, discount, gst, grand_total = calculate_bill(selected_costs, age)

    # Level 6: Invoice Generation
    print("\n-----------------------------------------------")
    print("HealWell Care Hospital")
    print("Patient Invoice")
    print("-----------------------------------------------")

    print(f"Name    : {name}")
    print(f"Age     : {age}")
    print(f"Gender  : {gender}")
    print(f"Contact : {contact}")

    print("\nServices Availed:")
    for i in range(len(selected_services)):
        print(f"{i+1}. {selected_services[i]} : ₹{selected_costs[i]}")

    print(f"\nSubtotal           : ₹{subtotal}")
    print(f"Discount Applied   : ₹{discount:.2f}")
    print(f"GST (18%)          : ₹{gst:.2f}")
    print(f"Grand Total        : ₹{grand_total:.2f}")

    print("\nThank you for choosing HealWell Care Hospital!")
    print("-----------------------------------------------")
