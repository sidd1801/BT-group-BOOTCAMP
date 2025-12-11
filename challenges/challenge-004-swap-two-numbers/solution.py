# solution.py

def swap_numbers(a, b):
    """
    Swap two numbers and return them as a tuple.
    """
    return b, a


if __name__ == "__main__":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    x, y = swap_numbers(x, y)

    print("After swapping:")
    print("First number =", x)
    print("Second number =", y)
