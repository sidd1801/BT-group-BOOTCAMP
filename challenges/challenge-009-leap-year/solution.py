# solution.py

def is_leap_year(year):
    """
    Returns True if the given year is a leap year, otherwise False.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


if __name__ == "__main__":
    year = int(input("Enter a year: "))

    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
