"""
Authors: Ben Huenemann and Michael Keyser

This file contains the algorithms for computing the longest subsequence
"""

"""
This is a wrapper function that takes in a sequence and a limit. It then calls the longest path algorithm for each
term in the sequence and keeps track of the maximum. At the end, it also converts the list of indices into values and
returns both. It also stops incrementing through the sequence if it reaches a point where the subsequence can't beat
the current maximum. The max_paths_length list is used to keep track of the maximum subsequence starting at each
element in the sequence.
"""
def longest_subsequence(sequence, limit):
    max_path = list()
    max_paths_list = [-1] * len(sequence)

    for i in range(0, len(sequence)):
        if i >= len(sequence) - len(max_path):
            break

        epsilon = abs(sequence[i] - limit)

        cur_path = longest_path(sequence, i, limit, epsilon + 1, 0, len(max_path), max_paths_list)
        if len(cur_path) > len(max_path):
            max_path = cur_path
    max_sequence = list(map(lambda n: sequence[n], max_path))
    return max_path, max_sequence


"""
This is where the main recursion occurs. Every iteration recalculates epsilon to be the distance between the start
value and the limit. If it is outside of the range, it returns an empty list. It also checks at the start to see if
the start is the last element of the series. If this is the case, it returns a list with just that element.

After these checks are completed, it iterates through the remaining terms in the sequence after the starting point.
If the longest path of a term hasn't been calculated left (if it's equal to -1) it calculates that term and updates it
in the max_paths_list. At the end it checks this against max sequence for the start term and updates it if it's longer.

Also note that whenever it recursively calls itself, it increments the current length and keeps track of the maximum
length that has been discovered so far for a minor optimization. This way it doesn't need to compute anything if it
isn't possible to beat the maximum subsequence.
"""
def longest_path(sequence, start, limit, epsilon, cur_length, max_len, max_paths_list):
    if abs(sequence[start] - limit) > epsilon:
        return list()
    if start == len(sequence):
        return [start]

    for i in range(start + 1, len(sequence)):
        if (cur_length + (len(sequence) - i)) <= max_len:
            break

        if max_paths_list[i] == -1:
            cur_path = longest_path(sequence, i, limit, abs(sequence[start] - limit),
                                         cur_length + 1, max_len, max_paths_list)
            if cur_path == -1:
                max_paths_list[i] = [i]
            elif len(cur_path) != 0:
                max_paths_list[i] = cur_path
            else:
                continue

        cur_path = [start] + max_paths_list[i]
        if max_paths_list[start] == -1 or len(cur_path) > len(max_paths_list[start]):
            max_paths_list[start] = cur_path

    return max_paths_list[start]
