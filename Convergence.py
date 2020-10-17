import sys

def longest_sequence(sequence):
    l_bound = sys.maxsize
    u_bound = -sys.maxsize

    for i in range(0, len(sequence)):
        if sequence[i] < l_bound:
            l_bound = sequence[i]
        if sequence[i] > u_bound:
            u_bound = sequence[i]

    for i in range(0, len(sequence)):
        longest_path(sequence, i)

def longest_path(sequence, start):