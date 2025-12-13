# solution.py

def min_of_array(arr):
    """
    Returns the minimum value in the array.
    """
    if len(arr) == 0:
        raise ValueError("Array is empty")
    return min(arr)


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        value = float(input(f"Enter element {i+1}: "))
        arr.append(value)

    print("Minimum value:", min_of_array(arr))
