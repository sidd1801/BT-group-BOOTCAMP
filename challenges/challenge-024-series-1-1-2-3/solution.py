# solution.py

def generate_series(n):
    result = []
    a, b = 1, 1

    while a <= n:
        result.append(a)
        a, b = b, a + b

    return result


if __name__ == "__main__":
    n = int(input("Enter N: "))
    print("Series:", generate_series(n))
