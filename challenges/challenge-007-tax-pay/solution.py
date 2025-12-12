# solution.py

def must_pay_tax(salary):
    """
    Returns True if salary > 300000 (3 lakhs), otherwise False.
    """
    return salary > 300000


if __name__ == "__main__":
    name = input("Enter your name: ")
    salary = float(input("Enter your salary: "))

    if must_pay_tax(salary):
        print(f"{name} must pay tax.")
    else:
        print(f"{name} does not need to pay tax.")
