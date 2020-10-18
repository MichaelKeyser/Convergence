import sys
import matplotlib as plt
def longest_sequence(sequence, limit):
    max_path = list()
    max_paths_list = [-1] * len(sequence)

    for i in range(0, len(sequence)):
        #print("Currently working on element", i)
        if i >= len(sequence) - len(max_path):
            break

        epsilon = abs(sequence[i] - limit)

        cur_path = longest_path(sequence, i, limit, epsilon + 1, 0, len(max_path), max_paths_list)
        if len(cur_path) > len(max_path):
            max_path = cur_path
    return max_path


def longest_path(sequence, start, limit, epsilon, cur_length, max_len, max_paths_list):
    if abs(sequence[start] - limit) > epsilon:
        return list()
    if start == len(sequence):
        return [sequence[start]]

    for i in range(start + 1, len(sequence)):
        if (cur_length + (len(sequence) - i)) <= max_len:
            break

        if max_paths_list[i] == -1:
            cur_path = longest_path(sequence, i, limit, abs(sequence[start] - limit),
                                         cur_length + 1, max_len, max_paths_list)
            if cur_path == -1:
                max_paths_list[i] = [sequence[i]]
            elif len(cur_path) != 0:
                max_paths_list[i] = cur_path
            else:
                continue

        cur_path = [sequence[start]] + max_paths_list[i]
        if max_paths_list[start] == -1 or len(cur_path) > len(max_paths_list[start]):
            max_paths_list[start] = cur_path

    return max_paths_list[start]
