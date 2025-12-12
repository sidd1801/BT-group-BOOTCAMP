# solution.py

def calculate_tax(taxable):
    """
    Simple tax calculation based on New Tax Regime 2023.
    No surcharge, no cess for simplicity.
    """

    if taxable <= 300000:
        return 0
    elif taxable <= 600000:
        return (taxable - 300000) * 0.05
    elif taxable <= 900000:
        return (300000 * 0.05) + (taxable - 600000) * 0.10
    elif taxable <= 1200000:
        return (300000 * 0.05) + (300000 * 0.10) + (taxable - 900000) * 0.15
    elif taxable <= 1500000:
        return (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (taxable - 1200000) * 0.20
    else:
        return (
            (300000 * 0.05)
            + (300000 * 0.10)
            + (300000 * 0.15)
            + (300000 * 0.20)
            + (taxable - 1500000) * 0.30
        )


def generate_report(name, monthly_salary):
    """
    Generates tax report for an employee based on monthly salary.
    """

    annual_salary = monthly_salary * 12
    standard_deduction = 50000

    taxable_income = max(0, annual_salary - standard_deduction)
    tax_payable = calculate_tax(taxable_income)
    net_income = annual_salary - tax_payable

    return {
        "name": name,
        "annual_salary": annual_salary,
        "taxable_income": taxable_income,
        "tax_payable": round(tax_payable, 2),
        "net_income": round(net_income, 2)
    }


if __name__ == "__main__":
    name = input("Enter employee name: ")
    monthly = float(input("Enter monthly salary: "))

    report = generate_report(name, monthly)

    print("\n----- TAX REPORT -----")
    print("Name:", report["name"])
    print("Annual Salary:", report["annual_salary"])
    print("Taxable Income:", report["taxable_income"])
    print("Tax Payable:", report["tax_payable"])
    print("Net Annual Income:", report["net_income"])
