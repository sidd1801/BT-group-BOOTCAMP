def generate_series(n):
    result = []
    num = 1
    sign = 1

    # Always include 1 if n >= 1
    if n >= 1:
        result.append(1)

    num += 4
    sign = -1

    while True:
        term = num * sign

        # Stop if term magnitude exceeds N
        if abs(term) > n:
            break

        # Skip adding the positive term equal to N
        if term == n and term > 0:
            break

        result.append(term)

        num += 4
        sign *= -1

    return result
