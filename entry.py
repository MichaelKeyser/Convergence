"""
This script serves as the entry to our project. It asks the user to enter in the number of elements of the sequence
along with the option to generate a random sequence.
"""
import setup as s

num_elements = input("How many elements do you want in your sequence: ")
sequence = input("Enter the sequence, or type RANDOM to generate a random sequence: ")

try:
    if sequence == "RANDOM":
        print("RANDOM")
    else:
        num_elements = int(num_elements) # this is an integer
except:
    print("Input could not be understood. Check your input format.")
