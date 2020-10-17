"""
This script serves as the entry to our project. It asks the user to enter in the number of elements of the sequence
along with the option to generate a random sequence.
"""


user = input("Please enter how many numbers you want in your sequence and provide a sequence. Please separate by comma. Type RANDOM if you want a random sequence: ")

try:
    if user == "RANDOM":
        print("RANDOM")
    else:
        user_input = user.split(",") # split at comma
        num_elements = input(user_input[0]) # this is an integer
        sequence = user_input[1] # this is a string
except:
    print("Input could not be understood. Check your input format.")
