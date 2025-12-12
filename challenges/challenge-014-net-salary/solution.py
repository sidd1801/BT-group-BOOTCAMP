# solution.py

def net_salary(annual_gross_salary, total_tax_payable):
    net = annual_gross_salary - total_tax_payable
    return {
        "annual_gross_salary": annual_gross_salary,
        "total_tax_payable": total_tax_payable,
        "annual_net_salary": net
    }


if __name__ == "__main__":
    gross = float(input("Enter Annual Gross Salary: "))
    tax = float(input("Enter Total Tax Payable (including cess): "))

    r = net_salary(gross, tax)

    print("\n--- NET SALARY REPORT ---")
    print("Annual Gross Salary:", r["annual_gross_salary"])
    print("Total Tax Payable:", r["total_tax_payable"])
    print("Annual Net Salary:", r["annual_net_salary"])
