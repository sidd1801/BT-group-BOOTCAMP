# solution.py

def number_increasing_repeat(n):
    """
    Returns a list of strings where each row contains
    the row number repeated row_number times.
    Example:
    1
    22
    333
    """
    return [str(i) * i for i in range(1, n + 1)]


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    for row in number_increasing_repeat(n):
        print(row)
