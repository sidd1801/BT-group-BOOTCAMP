# solution.py

def is_even(number):
    """
    Returns True if the number is even, False if odd.
    """
    return number % 2 == 0


if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if is_even(num):
        print(num, "is Even")
    else:
        print(num, "is Odd")
