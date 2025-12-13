# solution.py

def multiply_matrices(A, B):
    """
    Multiplies two matrices A and B.
    Returns the result matrix.
    """
    if not A or not B or len(A[0]) != len(B):
        raise ValueError("Invalid matrix dimensions for multiplication")

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)

    return result


if __name__ == "__main__":
    r1 = int(input("Enter rows of Matrix A: "))
    c1 = int(input("Enter columns of Matrix A: "))

    A = []
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input(f"A[{i}][{j}]: ")))
        A.append(row)

    r2 = int(input("Enter rows of Matrix B: "))
    c2 = int(input("Enter columns of Matrix B: "))

    B = []
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input(f"B[{i}][{j}]: ")))
        B.append(row)

    result = multiply_matrices(A, B)

    print("\nResultant Matrix:")
    for row in result:
        print(row)
