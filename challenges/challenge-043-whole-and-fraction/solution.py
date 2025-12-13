# solution.py

def split_number(value):
    """
    Splits a floating-point number into its whole part
    and fractional part.
    Example: 45.67 → (45, 0.67)
    """
    whole = int(value)
    fraction = value - whole
    return whole, fraction


if __name__ == "__main__":
    x = float(input("Enter a number: "))
    whole, frac = split_number(x)
    print("Whole part:", whole)
    print("Fractional part:", frac)
