import random as r


# generates a list of n random floating point numbers within lower_bound and upper_bound
def generate_sequence(lower, upper, n):
    sequence = []
    for i in range(n):
        sequence.append(r.uniform(lower,upper))
    return sequence
