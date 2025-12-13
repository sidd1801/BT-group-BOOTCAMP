# solution.py

def star_pattern(n):
    """
    Returns a list of strings, each containing n stars.
    Total n rows.
    """
    return ["*" * n for _ in range(n)]


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    for row in star_pattern(n):
        print(row)
