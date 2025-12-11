# solution.py
from decimal import Decimal

def calculate_simple_interest(P, R, T):
    P, R, T = Decimal(str(P)), Decimal(str(R)), Decimal(str(T))
    SI = (P * R * T) / Decimal("100")
    return float(SI)


if __name__ == "__main__":
    P = float(input("Enter Principal amount: "))
    R = float(input("Enter Rate of interest: "))
    T = float(input("Enter Time in years: "))

    SI = calculate_simple_interest(P, R, T)
    print("Simple Interest =", SI)
