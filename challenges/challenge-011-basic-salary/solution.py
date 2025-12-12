# solution.py

def calculate_salary(basic_salary, special_allowances, bonus_percentage):
    """
    Calculate:
    - Gross Monthly Salary
    - Annual Gross Salary (including bonus)
    """

    gross_monthly = basic_salary + special_allowances

    # Annual bonus is % of annual gross salary (without bonus)
    annual_without_bonus = gross_monthly * 12
    bonus_amount = annual_without_bonus * (bonus_percentage / 100)

    annual_gross_salary = annual_without_bonus + bonus_amount

    return {
        "gross_monthly_salary": gross_monthly,
        "annual_gross_salary": annual_gross_salary,
        "bonus_amount": bonus_amount,
    }


if __name__ == "__main__":
    name = input("Enter employee name: ")
    emp_id = input("Enter EmpID: ")
    basic = float(input("Enter Basic Monthly Salary: "))
    allowance = float(input("Enter Special Allowances (Monthly): "))
    bonus_pct = float(input("Enter Bonus Percentage (% of Gross Annual Salary): "))

    result = calculate_salary(basic, allowance, bonus_pct)

    print("\n--- EMPLOYEE SALARY REPORT ---")
    print("Employee Name:", name)
    print("Employee ID:", emp_id)
    print("Gross Monthly Salary:", result["gross_monthly_salary"])
    print("Annual Gross Salary:", result["annual_gross_salary"])
    print("Bonus Amount:", result["bonus_amount"])
