This project was created by Ben Heunemann and Michael Keyser for the FALL 2020 U of U
hackathon-HackTheU. The goal of this project is to find the longest convergent subsequence
of a sequence of numbers. The Bolzano-Weierstrass theorem states that any bounded sequence
has a convergent subsequence. It is said a sequence converges {x_n} to L if 
|x_n - L| < epsilon, epsilon > 0. We provide a sequence and an L to try and converge upon. Sequences in math are infinite, while computers are finite. We approximate a sequence
by computing the first n (n is specified by the user) elements of the sequence. This means we provide no formal proof of a subsequence converging to L.


Version and Use:
This project was developed using Python 3.8. 
To run this project run entry.py and follow the prompts. Once in the directory containing the scripts the project can be run from Terminal with
>>> python3 entry.py

INCLUDE EXAMPLES HERE


Example Showing How A Finite Approximation Can Work:
Take {x_n} = 1/n. It is well known that 1/n -> 0.
If we choose to look at the first 1000 numbers in {x_n} 1/1, 1/2, 1/3, 1/4, 1/5, ... , 1/1000 we can observe the general trend of the sequence; it looks like it is converging to 0. This does not 
work in a strict mathematical sense but is sufficient for our purposes.

Our Algorithm:




Example How To Find Convergent Subsequence Given L:
Take {x_n} = {4.1, 5, 4, 3 ,2} and L = 3.5
We start with the first element, which is 4.1. We look to see if element 2 (5) is closer to L than element 1 was. |5-3.5| > |4.1-3.5|, so we skip 5. Now we go to element 3 (4). |4.1-3| >= |4 -3|, so element 3 is added to the sequence. We recursively apply this to element 2, and so forth. The longest path is updated every time a path is discovered. No path that with a maximum length less than the current maximum path is considered. We get the answer as {4.1, 4, 3}.


