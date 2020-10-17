import sys


def longest_sequence(sequence, limit):
    max_path = list()

    l_bound = sys.maxsize
    u_bound = -sys.maxsize

    for i in range(0, len(sequence)):
        if sequence[i] < l_bound:
            l_bound = sequence[i]
        if sequence[i] > u_bound:
            u_bound = sequence[i]

    for i in range(0, len(sequence)):
        if i >= len(sequence) - len(max_path):
            break

        epsilon = abs(sequence[i] - limit)

        cur_path = longest_path(sequence, i, limit, epsilon + 1, len(max_path))
        if len(cur_path) > len(max_path):
            max_path = cur_path
    return max_path


def longest_path(sequence, start, limit, epsilon, max_len):
    if abs(sequence[start] - limit) >= epsilon:
        return list()
    if start == len(sequence):
        return list(range(start, start + 1))

    max_path = list()
    for i in range(start + 1, len(sequence)):
        cur_path = list(range(start, start + 1)) + longest_path(sequence, i, limit, abs(sequence[start] - limit), max_len)
        if len(cur_path) > len(max_path):
            max_path = cur_path
    return max_path


#print(longest_sequence([1, 9, 4, 5, 2, 9, 4, 5, 2, 4, 2], 5))
