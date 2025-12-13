# solution.py

def number_pattern_same(n):
    """
    Returns a list of strings where each row contains
    the same number repeated n times.
    """
    return [str(i) * n for i in range(1, n + 1)]


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    for row in number_pattern_same(n):
        print(row)
