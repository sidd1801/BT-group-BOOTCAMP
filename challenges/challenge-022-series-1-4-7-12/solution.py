# solution.py

def generate_series(n):
    diffs = [3, 3, 5]  # given known pattern
    result = []
    current = 1
    diff_index = 0

    while current <= n:
        result.append(current)

        if diff_index < len(diffs):
            next_diff = diffs[diff_index]
            diff_index += 1
        else:
            # pattern continues as diff = diff * 2 + 1
            next_diff = diffs[-1] * 2 + 1
            diffs.append(next_diff)

        current = current + next_diff

    return result
