"""
This script contains functions that generate sequences to be searched for the longest subsequence. It also contains functions used for graphing the sequences.
Authors:
"""

import random as r

"""
Generates a list of n random floating point numbers within lower_bound and upper_bound
"""
def generate_random_sequence(lower, upper, n):
    sequence = []
    for i in range(n):
        sequence.append(r.uniform(lower,upper))
    return sequence
"""
Generates a sequence provided the definition and number of elements passed by the user
"""
def generate_specific_sequence(sequence_definition, num_elements):
    sequence = []
    for n in range(num_elements):
        n = n + 1 # sequences start at 1 instead of 0 and end at num_elements instead of num_elements - 1
        val = float(eval(sequence_definition)) # be aware that eval can be a potentially dangerous function to use
        sequence.append(val)
    return sequence


def graph(indices, longest_seq, seq):
    import matplotlib.pyplot as plt # import inline is done here in case user does not have matplotlib installed, can choose to not graph
    plt.scatter(indices, longest_seq)
    plt.scatter([i + 1 for i in range(len(seq))], seq)
    plt.show()
