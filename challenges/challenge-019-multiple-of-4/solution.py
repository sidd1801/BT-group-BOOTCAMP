# solution.py

def generate_even_squares(n):
    result = []
    i = 2
    while i*i <= n:
        result.append(i*i)
        i += 2
    return result


if __name__ == "__main__":
    n = int(input("Enter N: "))
    series = generate_even_squares(n)
    print("Series:", series)
