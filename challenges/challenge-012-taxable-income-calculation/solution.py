# solution.py

def calculate_taxable_income(annual_gross_salary):
    """
    Deducts standard deduction of ₹50,000
    and returns taxable income + intermediate values.
    """
    standard_deduction = 50000

    # Standard deduction cannot exceed gross salary
    deduction_applied = min(standard_deduction, annual_gross_salary)

    taxable_income = annual_gross_salary - deduction_applied

    return {
        "annual_gross_salary": annual_gross_salary,
        "standard_deduction": deduction_applied,
        "taxable_income": taxable_income
    }


if __name__ == "__main__":
    annual_salary = float(input("Enter Annual Gross Salary: "))

    result = calculate_taxable_income(annual_salary)

    print("\n--- TAXABLE INCOME REPORT ---")
    print("Annual Gross Salary:", result["annual_gross_salary"])
    print("Standard Deduction:", result["standard_deduction"])
    print("Taxable Income:", result["taxable_income"])
