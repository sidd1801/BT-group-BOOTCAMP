# solution.py

def slab_tax(taxable):
    tax = 0
    if taxable > 300000:
        tax += min(taxable, 600000) - 300000
        tax *= 0.05
    if taxable > 600000:
        tax += (min(taxable, 900000) - 600000) * 0.10
    if taxable > 900000:
        tax += (min(taxable, 1200000) - 900000) * 0.15
    if taxable > 1200000:
        tax += (min(taxable, 1500000) - 1200000) * 0.20
    if taxable > 1500000:
        tax += (taxable - 1500000) * 0.30
    return tax


def calculate_tax(taxable_income):
    tax_before_rebate = slab_tax(taxable_income)

    # Full rebate if taxable ≤ 7,00,000
    if taxable_income <= 700000:
        tax_after_rebate = 0
        rebate = tax_before_rebate
    else:
        tax_after_rebate = tax_before_rebate
        rebate = 0

    cess = tax_after_rebate * 0.04
    total = tax_after_rebate + cess

    return {
        "tax_before_rebate": round(tax_before_rebate, 2),
        "rebate": round(rebate, 2),
        "tax_after_rebate": round(tax_after_rebate, 2),
        "cess": round(cess, 2),
        "total_tax_payable": round(total, 2)
    }


if __name__ == "__main__":
    income = float(input("Enter taxable income: "))
    r = calculate_tax(income)

    print("\n--- TAX BREAKDOWN ---")
    print("Tax Before Rebate:", r["tax_before_rebate"])
    print("Rebate Applied:", r["rebate"])
    print("Tax After Rebate:", r["tax_after_rebate"])
    print("Cess (4%):", r["cess"])
    print("Total Tax Payable:", r["total_tax_payable"])
