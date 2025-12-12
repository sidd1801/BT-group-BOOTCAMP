# solution.py

def validate_name(name):
    if not name.strip():
        return False, "Name cannot be empty"
    if len(name) > 50:
        return False, "Name too long"
    if not name.replace(" ", "").isalpha():
        return False, "Name must contain alphabets only"
    return True, name


def validate_empid(empid):
    if not empid.isalnum():
        return False, "EmpID must be alphanumeric"
    if not (5 <= len(empid) <= 10):
        return False, "EmpID must be 5–10 characters"
    return True, empid


def validate_basic_salary(basic):
    try:
        value = float(basic)
    except:
        return False, "Basic salary must be a number"
    if value <= 0:
        return False, "Basic salary must be positive"
    if value > 10000000:
        return False, "Basic salary too large"
    return True, value


def validate_allowances(allow):
    try:
        value = float(allow)
    except:
        return False, "Allowances must be a number"
    if value < 0:
        return False, "Allowances cannot be negative"
    if value > 10000000:
        return False, "Allowances too large"
    return True, value


def validate_bonus(bonus):
    try:
        value = float(bonus)
    except:
        return False, "Bonus % must be a number"
    if value < 0 or value > 100:
        return False, "Bonus % must be between 0 and 100"
    return True, value


def calculate_gross_monthly(basic, allowances):
    return basic + allowances


def calculate_annual_gross(gross_monthly, bonus_pct):
    annual = gross_monthly * 12
    bonus_amount = annual * (bonus_pct / 100)
    return annual + bonus_amount


def validate_derived(gms, annual):
    if gms <= 0:
        return False, "Gross monthly salary must be greater than 0"
    if annual > 50000000:  # simple upper limit
        return False, "Annual salary unrealistically high"
    return True, ""


def get_valid_input(prompt, validator):
    while True:
        value = input(prompt)
        ok, result = validator(value)
        if ok:
            return result
        print("Invalid:", result)


if __name__ == "__main__":
    name = get_valid_input("Enter Name: ", validate_name)
    empid = get_valid_input("Enter EmpID: ", validate_empid)
    basic = get_valid_input("Enter Basic Salary: ", validate_basic_salary)
    allowances = get_valid_input("Enter Allowances: ", validate_allowances)
    bonus_pct = get_valid_input("Enter Bonus %: ", validate_bonus)

    gms = calculate_gross_monthly(basic, allowances)
    annual = calculate_annual_gross(gms, bonus_pct)

    ok, msg = validate_derived(gms, annual)
    if not ok:
        print("Error:", msg)
    else:
        print("\n--- VALIDATION SUCCESSFUL ---")
        print("Name:", name)
        print("EmpID:", empid)
        print("Gross Monthly Salary:", gms)
        print("Annual Gross Salary:", annual)
