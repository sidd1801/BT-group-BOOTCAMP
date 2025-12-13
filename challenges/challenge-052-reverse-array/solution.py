# solution.py

def reverse_array(arr):
    """
    Returns the reversed version of the array.
    """
    return arr[::-1]


if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        value = input(f"Enter element {i+1}: ")
        arr.append(value)

    print("Reversed array:", reverse_array(arr))
