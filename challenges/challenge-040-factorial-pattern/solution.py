# solution.py

import math

def factorial_pattern(n):
    """
    Returns a list of rows where factorials
    are printed in increasing sequence.
    Example (n = 3):
    1
    1 2
    6 24 120
    """
    num = 1
    output = []

    for row_len in range(1, n + 1):
        row = []
        for _ in range(row_len):
            row.append(math.factorial(num))
            num += 1
        output.append(row)

    return output


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    pattern = factorial_pattern(n)
    for row in pattern:
        print(*row)
