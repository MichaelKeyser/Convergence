import random as r


# generates a list of n random floating point numbers within lower_bound and upper_bound
def generate_random_sequence(lower, upper, n):
    sequence = []
    for i in range(n):
        sequence.append(r.uniform(lower,upper))
    return sequence

def generate_specific_sequence(sequence_definition, num_elements):
    sequence = []
    for n in range(num_elements):
        n = n + 1 # sequences start at 1 instead of 0 and end at num_elements instead of num_elements - 1
        val = float(eval(sequence_definition)) # be aware that eval can be a potentially dangerous function to use
        sequence.append(val)
    return sequence
