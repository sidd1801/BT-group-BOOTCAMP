# solution.py

def number_increasing_seq(n):
    """
    Returns a list of strings:
    1
    12
    123
    1234
    ...
    """
    return ["".join(str(j) for j in range(1, i + 1)) for i in range(1, n + 1)]


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    for row in number_increasing_seq(n):
        print(row)
