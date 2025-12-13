# solution.py

def sum_2d_array(matrix):
    """
    Returns the sum of all elements in a 2D array.
    """
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element [{i}][{j}]: ")))
        matrix.append(row)

    print("Sum of all elements:", sum_2d_array(matrix))
