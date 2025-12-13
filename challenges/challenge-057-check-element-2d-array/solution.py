# solution.py

def search_2d_array(matrix, target):
    """
    Returns True if target exists in the 2D array,
    otherwise returns False.
    """
    for row in matrix:
        if target in row:
            return True
    return False


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element [{i}][{j}]: ")))
        matrix.append(row)

    target = int(input("Enter element to search: "))

    if search_2d_array(matrix, target):
        print("Element found")
    else:
        print("Element not found")
