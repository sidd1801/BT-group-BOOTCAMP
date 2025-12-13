# solution.py

def max_of_array(arr):
    """
    Returns the maximum value in the array.
    """
    if len(arr) == 0:
        raise ValueError("Array is empty")
    return max(arr)


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        value = float(input(f"Enter element {i+1}: "))
        arr.append(value)

    print("Maximum value:", max_of_array(arr))
