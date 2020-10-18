Authors: Ben Huenemann and Michael Keyser
Project Start: 10/18/20
Project End: 10/19/29


Project Inspiration:
This project was created by Ben Huenemann and Michael Keyser for the FALL 2020 U of U
hackathon-HackTheU. We want to combine elements and ideas fram Real Analysis with concepts from computer science. This is interesting, because Real Analysis often deals with ideas and concepts that cannot be well represented using computers. One such example are sequences. Sequences are fundamental to the study of mathematics but cannot be represented on a computer, because they are infinite. We aim to approximate sequences and apply a longest path algorithm to find the longest convergent subsequence.


Background Math: 
The goal of this project is to find the longest convergent subsequence
of a sequence of numbers. The Bolzano-Weierstrass theorem states that any bounded sequence
has a convergent subsequence. It is said a sequence {x_n} converges to L if 
|x_n - L| < epsilon, epsilon > 0. We provide a sequence and an L to try and converge upon. Sequences in math are infinite, while computers are finite. We approximate a sequence
by computing the first n (n is specified by the user) elements of the sequence. This means we provide no formal proof of a subsequence converging to L.


Example How To Find A Convergent Subsequence Given L:
Take {x_n} = {4.1, 5, 4, 3 ,2} and L = 3.5. We start with the first element, which is 4.1. We look to see if element 2 (5) is closer to L than element 1 was. |5-3.5| > |4.1-3.5|, so we skip 5. Now we go to element 3 (4). |4.1-3| >= |4 -3|, so element 3 is added to the sequence. We recursively apply this to element 2, and so forth. The longest path is updated every time a path is discovered. No path that with a maximum length less than the current maximum path is considered. We get the answer as {4.1, 4, 3}.


Example Showing How A Finite Approximation Can Work:
Take {x_n} = 1/n. It is well known that 1/n -> 0.
If we choose to look at the first 1000 numbers in {x_n} 1/1, 1/2, 1/3, 1/4, 1/5, ... , 1/1000 we can observe the general trend of the sequence; it looks like it is converging to 0. This does not work in a strict mathematical sense but is sufficient for our purposes.


Our Algorithm:
This project only counts sequences that get closer to the desired limit.
In order to make it more of an optimization problem, we made it calculate the longest sequence that converges to that limit. This could be used to find potential subsequences when plugging in infinite sequences. Another optimization would have to be added, however, to find the limit that has the longest convergent series.

The way that the algorithm accomplishes this is by computing all of the subsequences recursively and eliminating ones that don't satisfy convergence. While it does this, it keeps track of a list of the maximum sequences for each entry in the sequence so it doesn't have to repeat the computations. It also doesn't bother computing sequences when there aren't enough elements left to beat the current maximum.


Version and Use:
This project was developed using Python 3.8. 
To run this project run entry.py and follow the prompts. Once in the directory containing the scripts the project can be run from Terminal with 
python3 entry.py 
Command line arguments can be passed. 
entry.py p 
will print the longest sequence, 
entry.py g
will graph the sequence and the longest sequence. Entering 
entry.py p g 
will print the longest sequence and graph it. Matplotlib is required for the plots to be generated. Do not pass g as a command line argument if Matplotlib is not installed. The other functionality still works with only standard Python libraries. 

The user will be prompted to provide the number of elements in the sequence that will be searched for a subsequence. The user will then be prompted to enter either "RANDOM" or a sequence using proper python syntax. For example, (1 + n)/ n is allowed. Entering "RANDOM" (no quotes when entering input) will also ask for the lower and upper bound to generate the random numbers between. Floating point values are allowed.

A user define sequence is evaluated using Python's eval() function. This means that sequences can be defined using Python's math library. For example, math.log(n) works too. 


RecusrionError:
It is possible that a RecursionError can occur. This will happen when a significant portion
of the longest subsequence are part of the base sequence that is being searched. For example. 1/n with -> 0 uses all elements in the sequence to construct the longest path. 1/n -> 0 does not work for n = 1000. However, a random sequence avoids this issue and has been tested up to
n = 10000 with a lower bound of -10, upper bound of 0, and a desired limit of 0. 

Examples:
image number # elements lower_bound upper_bound  limit     sequence_definition

example1.png    10000      -10          10         0
example2.png    1000       -10          10         -10
example3.png    100        n/a          n/a        0	      1/n
example4.png    50         0            10         5  
example5.png    1000       n/a          n/a        0          math.sin(n)
example6.png    1000       n/a          n/a        50         math.tan(n)








