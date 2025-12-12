# solution.py

def gross_monthly_salary(basic, allowances):
    return basic + allowances


def annual_salary(gross_monthly):
    return gross_monthly * 12


def taxable_income(annual_gross):
    deduction = 50000
    return max(0, annual_gross - deduction)


def slab_tax(taxable):
    tax = 0
    if taxable > 300000:
        tax += (min(taxable, 600000) - 300000) * 0.05
    if taxable > 600000:
        tax += (min(taxable, 900000) - 600000) * 0.10
    if taxable > 900000:
        tax += (min(taxable, 1200000) - 900000) * 0.15
    if taxable > 1200000:
        tax += (min(taxable, 1500000) - 1200000) * 0.20
    if taxable > 1500000:
        tax += (taxable - 1500000) * 0.30
    return tax


def tax_breakdown(taxable):
    before_rebate = slab_tax(taxable)

    if taxable <= 700000:
        rebate = before_rebate
        after_rebate = 0
    else:
        rebate = 0
        after_rebate = before_rebate

    cess = after_rebate * 0.04
    total_tax = after_rebate + cess

    return {
        "tax_before_rebate": round(before_rebate, 2),
        "rebate": round(rebate, 2),
        "tax_after_rebate": round(after_rebate, 2),
        "cess": round(cess, 2),
        "total_tax": round(total_tax, 2)
    }


def net_salary(annual_gross, total_tax):
    return annual_gross - total_tax


def generate_report(name, empid, basic, allowances):
    gms = gross_monthly_salary(basic, allowances)
    annual = annual_salary(gms)
    taxable = taxable_income(annual)
    tax = tax_breakdown(taxable)
    net = net_salary(annual, tax["total_tax"])

    return {
        "name": name,
        "empid": empid,
        "gross_monthly_salary": gms,
        "annual_gross_salary": annual,
        "taxable_income": taxable,
        "tax_payable": tax["total_tax"],
        "annual_net_salary": net,
        "breakdown": tax
    }


def print_report(report):
    print("\nEmployee Tax Report\n")
    print(f"{'Field':<25} Details")
    print("-" * 45)
    print(f"{'Name':<25} {report['name']}")
    print(f"{'EmpID':<25} {report['empid']}")
    print(f"{'Gross Monthly Salary':<25} ₹{report['gross_monthly_salary']:,}")
    print(f"{'Annual Gross Salary':<25} ₹{report['annual_gross_salary']:,}")
    print(f"{'Taxable Income':<25} ₹{report['taxable_income']:,}")
    print(f"{'Tax Payable':<25} ₹{report['taxable_income']:,}")
    print(f"{'Annual Net Salary':<25} ₹{report['annual_net_salary']:,}")


if __name__ == "__main__":
    name = input("Enter Name: ")
    empid = input("Enter EmpID: ")
    basic = float(input("Enter Basic Monthly Salary: "))
    allowances = float(input("Enter Special Allowances: "))

    r = generate_report(name, empid, basic, allowances)
    print_report(r)
