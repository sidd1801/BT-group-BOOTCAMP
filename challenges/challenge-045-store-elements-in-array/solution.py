# solution.py

def store_elements(n, elements):
    """
    Accepts n and a list of n elements.
    Returns the array as is.
    """
    if len(elements) != n:
        raise ValueError("Number of elements does not match n")
    return elements


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []
    for i in range(n):
        value = input(f"Enter element {i+1}: ")
        arr.append(value)

    print("Stored array:", arr)
