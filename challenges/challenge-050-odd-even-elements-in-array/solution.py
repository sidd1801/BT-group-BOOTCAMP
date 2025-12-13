# solution.py

def count_even_odd(arr):
    """
    Counts even and odd numbers in the array.
    Returns a tuple: (even_count, odd_count)
    """
    even = 0
    odd = 0

    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        value = int(input(f"Enter element {i+1}: "))
        arr.append(value)

    even, odd = count_even_odd(arr)
    print("Even numbers:", even)
    print("Odd numbers:", odd)
