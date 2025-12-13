# solution.py

def create_matrix(m, n, elements):
    """
    Creates an m x n matrix from the given elements list.
    """
    if len(elements) != m * n:
        raise ValueError("Number of elements does not match matrix size")

    matrix = []
    index = 0
    for _ in range(m):
        row = elements[index:index + n]
        matrix.append(row)
        index += n

    return matrix


def transpose_matrix(matrix):
    """
    Returns the transpose of the given matrix.
    """
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        transpose.append(row)

    return transpose


if __name__ == "__main__":
    m = int(input("Enter number of rows (M): "))
    n = int(input("Enter number of columns (N): "))

    elements = []
    for i in range(m * n):
        elements.append(int(input(f"Enter element {i+1}: ")))

    matrix = create_matrix(m, n, elements)
    transposed = transpose_matrix(matrix)

    print("\nMatrix:")
    for row in matrix:
        print(row)

    print("\nTranspose:")
    for row in transposed:
        print(row)
