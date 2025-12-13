# solution.py

def sort_array(arr, order):
    """
    Sorts the array in ascending or descending order.

    order = "asc"  → ascending
    order = "desc" → descending
    """
    if order == "asc":
        return sorted(arr)
    elif order == "desc":
        return sorted(arr, reverse=True)
    else:
        raise ValueError("Order must be 'asc' or 'desc'")
    

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        value = int(input(f"Enter element {i+1}: "))
        arr.append(value)

    order = input("Enter sorting order (asc/desc): ").lower()

    print("Sorted array:", sort_array(arr, order))
