# solution.py

def generate_series(n):
    result = []
    current = 1

    increments = [4, 4, 4, 8]
    cycle_count = 0  # how many full cycles completed
    idx = 0

    while current <= n:
        result.append(current)

        # After completing 2 full cycles, allow only 1 more increment then stop
        if cycle_count >= 2 and idx == 1:
            break

        next_val = current + increments[idx]
        if next_val > n:
            break

        current = next_val
        idx += 1

        # cycle completed
        if idx == 4:
            idx = 0
            cycle_count += 1

    return result
