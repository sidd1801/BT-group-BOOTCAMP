# solution.py

def generate_series(n):
    result = []
    current = 1
    diff = 3

    while current <= n:
        result.append(current)
        next_value = current + diff
        diff = diff * 2 - 1
        current = next_value

    return [x for x in result if x <= n]


if __name__ == "__main__":
    n = int(input("Enter N: "))
    print("Series:", generate_series(n))
