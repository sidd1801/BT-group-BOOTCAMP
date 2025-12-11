"""
challenge-001-sum-average/solution.py
Problem: Given two numbers a and b, return their sum and average.
Language: Python
Return format: (sum, average) where average is a float if needed.
"""

from typing import Tuple

def sum_and_average(a: float, b: float) -> Tuple[float, float]:
    """
    Return (sum, average) of two numbers.
    This function accepts ints or floats.
    """
    s = a + b
    avg = s / 2
    return s, avg

if __name__ == "__main__":
    # simple interactive demo (not used by tests)
    import sys
    if len(sys.argv) >= 3:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        s, avg = sum_and_average(a, b)
        print(f"sum={s}, average={avg}")
    else:
        print("Usage: python solution.py <num1> <num2>")
