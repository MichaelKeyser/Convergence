"""
This script serves as the entry to our project. It asks the user to enter in the number of elements of the sequence
along with the option to generate a random sequence.
"""

import functions as f
import convergence as c

num_elements = input("How many elements do you want in your sequence: ")
sequence = input("Enter the sequence with n as the variable, or type RANDOM to generate a random sequence: ")
limit = input("Enter the limit you want to converge to: ")
"""
try:
    if sequence == "RANDOM":
        lower = input("Provide lower bound: ")
        lower = float(lower.strip())
        upper = input("Provide upper bound: ")
        upper = float(upper.strip())
        seq = generate_random_sequence(lower, uppper, int(num_elements))
    else:
        num_elements = int(num_elements) # this is an integer
except:
    print("Input could not be understood. Check your input format.")
"""
limit = float(limit)
if sequence == "RANDOM":
    lower = input("Provide lower bound: ")
    lower = float(lower.strip())
    upper = input("Provide upper bound: ")
    upper = float(upper.strip())
    seq = f.generate_random_sequence(lower, upper, int(num_elements))
    longest_seq = c.longest_sequence(seq, limit)
else:
    seq = f.generate_specific_sequence(sequence, int(num_elements))
    longest_seq = c.longest_sequence(seq, limit)
print("Longest Sequence: ", longest_seq)
