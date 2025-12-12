# solution.py

def largest_of_three(a, b, c):
    """
    Returns the largest of three numbers.
    """
    return max(a, b, c)


if __name__ == "__main__":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    z = float(input("Enter third number: "))

    largest = largest_of_three(x, y, z)
    print("The largest number is:", largest)
