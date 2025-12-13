# solution.py

def binary_search(arr, target):
    """
    Performs binary search on a sorted array.
    Returns True if target is found, else False.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        value = int(input(f"Enter element {i+1}: "))
        arr.append(value)

    arr.sort()  # binary search needs sorted array
    print("Sorted array:", arr)

    target = int(input("Enter element to search: "))

    if binary_search(arr, target):
        print("Element found")
    else:
        print("Element not found")
