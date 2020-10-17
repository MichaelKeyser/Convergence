# Convergence
This project was created by Ben Heunemann and Michael Keyser for the FALL 2020 U of U
hackathon-HackTheU. The goal of this project is to find the longest convergent subsequence
of a sequence of numbers. The Bolzano-Weierstrass theorem states that any bounded sequence
has a convergent subsequence. It is said a sequence converges {x_n} if 
|x_n - L| < epsilon, epsilon > 0. We provide a sequence and an L to try and converge upon. This violates the strict definition of convergence, but can provide a good finite approximation. 

Example Showing How A Finite Approximation Can Work:
Take {x_n} = 1/n. It is well known that 1/n -> 0.
If we choose to look at the first 1000 numbers in {x_n} 1/1, 1/2, 1/3, 1/4, 1/5, ... , 1/1000 we can observe the general trend of the sequence; it looks like it is converging to 0. This does not work in mathematics but is sufficient for an approximation.

Our algorithm




Example How To Find Convergent Subsequence Given L:
Take {x_n} = 1/n and suppose we provide L = 0. We will use the first 1000 values of {x_n}
{x_n} = 1/1, 1/3, 1/4, ...., 1/1000, 
n = 1: 1
n = 2: 1/2
n = 3: 1/3 
.
.
.
n = 1000: 1/1000
The distance between n = 1 and n = 2 is 1/2. 