# solution.py

def fibonacci_pattern(n):
    """
    Returns a list of lists forming a Fibonacci triangle pattern.
    Example for n = 4:
    1
    1 2
    3 5 8
    13 21 34 55
    """
    a, b = 1, 1
    output = []

    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            row.append(a)
            a, b = b, a + b
        output.append(row)

    return output


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    pattern = fibonacci_pattern(n)
    for row in pattern:
        print(*row)
