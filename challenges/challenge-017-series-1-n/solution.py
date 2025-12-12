# solution.py

def generate_series(n):
    return list(range(1, n + 1))


if __name__ == "__main__":
    n = int(input("Enter N: "))
    series = generate_series(n)
    print("Series:", series)
