# solution.py

def search_element(arr, target):
    """
    Searches for 'target' in the array.
    Returns True if found, False otherwise.
    """
    return target in arr


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        value = input(f"Enter element {i+1}: ")
        arr.append(value)

    target = input("Enter element to search: ")

    if search_element(arr, target):
        print("Element found")
    else:
        print("Element not found")
