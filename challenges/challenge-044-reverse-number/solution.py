# solution.py

def reverse_number(num):
    """
    Returns the reverse of an integer.
    Handles negative numbers correctly.
    Example: -123 → -321
    """
    sign = -1 if num < 0 else 1
    num = abs(num)
    reversed_num = int(str(num)[::-1])
    return sign * reversed_num
