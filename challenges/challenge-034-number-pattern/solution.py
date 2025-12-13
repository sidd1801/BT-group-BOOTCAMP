# solution.py

def number_pattern_seq(n):
    """
    Returns a list of strings where each row contains
    the sequence 1 to n.
    Example for n=5: "12345"
    """
    row = "".join(str(i) for i in range(1, n + 1))
    return [row for _ in range(n)]


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    for line in number_pattern_seq(n):
        print(line)
