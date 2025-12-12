# solution.py

def generate_series(n):
    result = []
    i = 1

    while i * i <= n:
        if i % 4 != 0:          # skip multiples of 4
            result.append(i * i)
        i += 1

    return result


if __name__ == "__main__":
    n = int(input("Enter N: "))
    print("Series:", generate_series(n))
