# solution.py

def generate_series(n):
    result = []
    current = 1
    increment = 1

    while current <= n:
        result.append(current)
        current += increment
        increment += 1

    return result


if __name__ == "__main__":
    n = int(input("Enter N: "))
    print("Series:", generate_series(n))
