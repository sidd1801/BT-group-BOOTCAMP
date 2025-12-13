# solution.py

def star_increasing(n):
    """
    Returns a list of strings where each row
    contains increasing number of stars.
    """
    return ["*" * i for i in range(1, n + 1)]


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    for row in star_increasing(n):
        print(row)
