# solution.py

def create_2d_array(rows, cols, elements):
    """
    Creates a 2D array with given rows and columns
    using elements list.
    """
    if len(elements) != rows * cols:
        raise ValueError("Number of elements does not match matrix size")

    matrix = []
    index = 0
    for _ in range(rows):
        row = elements[index:index + cols]
        matrix.append(row)
        index += cols

    return matrix


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    elements = []
    for i in range(rows * cols):
        elements.append(int(input(f"Enter element {i+1}: ")))

    matrix = create_2d_array(rows, cols, elements)

    print("\n2D Array (Row-wise):")
    for row in matrix:
        print(row)
