# solution.py

def generate_odd_series(n):
    return [i for i in range(1, n + 1, 2)]


if __name__ == "__main__":
    n = int(input("Enter N: "))
    series = generate_odd_series(n)
    print("Series:", series)
