This project was created by Ben Huenemann and Michael Keyser for the FALL 2020 U of U
hackathon-HackTheU. The goal of this project is to find the longest convergent subsequence
of a sequence of numbers. The Bolzano-Weierstrass theorem states that any bounded sequence
has a convergent subsequence. It is said a sequence converges {x_n} to L if 
|x_n - L| < epsilon, epsilon > 0. We provide a sequence and an L to try and converge upon. Sequences in math are infinite, while computers are finite. We approximate a sequence
by computing the first n (n is specified by the user) elements of the sequence. This means we provide no formal proof of a subsequence converging to L.

This project also only counts sequences that get closer to the desired limit.
In order to make it more of an optimization problem, we made it calculate the longest sequence
that converges to that limit. This could used to find potential subsequences when plugging
in infinite sequences. Another optimization would have to be added, however, to find the limit
that has the longest convergent series.

The way that the algorithm accomplishes this is by computing all of the subsequences recursively
and eliminating ones that don't satisfy convergence. While it does this, it keeps track of
a list of the maximum sequences for each entry in the sequence so it doesn't have to repeat
the computations. It also doesn't bother computing sequences when there aren't enough elements
left to beat the current maximum.

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


