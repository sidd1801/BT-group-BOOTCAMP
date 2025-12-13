# solution.py

def sum_of_array(arr):
    """
    Returns the sum of all elements in the array.
    """
    return sum(arr)


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        value = float(input(f"Enter element {i+1}: "))
        arr.append(value)

    print("Sum of array elements:", sum_of_array(arr))
