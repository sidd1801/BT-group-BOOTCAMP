# solution.py

def perfect_square_pattern(n):
    num = 1
    output = []

    for row_num in range(1, n + 1):
        row = []
        
        # Determine starting sign based on row number
        if row_num % 4 in (1, 0):   # rows 1,4,5,8,... start positive
            sign = 1
        else:                       # rows 2,3,6,7,... start negative
            sign = -1

        for j in range(row_num):
            val = (num * num) * sign
            row.append(val)
            sign *= -1   # alternate sign
            num += 1

        output.append(row)

    return output
