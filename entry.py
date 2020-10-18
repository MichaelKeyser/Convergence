"""
Authors: Ben Huenemann and Michael Keyser
This script serves as the entry to our project. It asks the user to enter in the
number of elements of the sequence along with the option to generate a random
sequence. It also takes command line arguments to determine the output. If the
command line argument is p the longest sequence will be printed.
"""

import functions as f
import convergence as c
import sys

# number of elements to be in sequence
num_elements = input("How many elements do you want in your sequence: ")
# the sequence as a string, eg. 1/n
sequence = input("Enter the sequence with n as the variable, or type RANDOM to generate a random sequence: ")
# what limit we want to converg to
limit = input("Enter the limit you want to converge to: ")

try:
    limit = float(limit)
    seq = []
    longest_seq = []
    indices = []
    if sequence == "RANDOM": # the user provided RANDOM as the sequence
        lower = input("Provide lower bound: ") # ask for a lower bound
        lower = float(lower.strip())
        upper = input("Provide upper bound: ") # ask for an upper bound
        upper = float(upper.strip())
        seq = f.generate_random_sequence(lower, upper, int(num_elements)) # generate a random sequence given the upper and lower bound
        indices, longest_seq = c.longest_subsequence(seq, limit) # find the longest subsequence
    else: # user provided a sequence, e.g. 1/n
        seq = f.generate_specific_sequence(sequence, int(num_elements)) # generate the sequence using the sequence definition provided by user
        indices, longest_seq = c.longest_subsequence(seq, limit) # find the longest subsequence

    num_args = len(sys.argv)
    if(num_args > 1): # user provided a command line argument
        if str(sys.argv[1]) == "p": # check if first command line argument was p
            print("Longest Sequence: ", longest_seq)
        elif str(sys.argv[1]) == "g":
            f.graph(indices, longest_seq, seq)
    if(num_args == 3): # user provided 2 command line arguments
        if(str(sys.argv[2]) == "g"): # check if second command line argument was g
            f.graph(indices, longest_seq, seq)
except RecursionError as err:
    print("A RecursionError ocurred when finding the longest sequence. Please choose a less intensive sequence as described in the README.")
except:
    print("An error ocurred. Check your input format.\nCheck all command line arguments and inputs adhere to specifications in the README.")
