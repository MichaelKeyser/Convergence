def longest_sequence(sequence, limit):
    max_path = list()

    for i in range(0, len(sequence)):
        if i >= len(sequence) - len(max_path):
            break

        epsilon = abs(sequence[i] - limit)

        cur_path = longest_path(sequence, i, limit, epsilon + 1, 0, len(max_path))
        if len(cur_path) > len(max_path):
            max_path = cur_path
    return max_path


def longest_path(sequence, start, limit, epsilon, cur_length, max_len):
    if abs(sequence[start] - limit) >= epsilon:
        return list()
    if start == len(sequence):
        return list(str(sequence[start]))

    max_path = list()
    for i in range(start + 1, len(sequence)):
        if (cur_length + (len(sequence) - i)) <= max_len:
            break

        cur_path = list(str(sequence[start]))\
                   + longest_path(sequence, i, limit, abs(sequence[start] - limit), cur_length + 1, max_len)
        if len(cur_path) > len(max_path):
            max_path = cur_path
    return max_path


#print(longest_sequence([1, 9, 4, 5, 2, 9, 4, 5, 2, 4, 2], 5))
