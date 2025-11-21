"""
Given an array X of positive integers, its elements are to be transformed by running the following operation on them as many times as required:

if X[i] > X[j] then X[i] = X[i] - X[j]

When no more transformations are possible, return its sum ("smallest possible sum").

For instance, the successive transformation of the elements of input X = [6, 9, 21] is detailed below:

X_1 = [6, 9, 12] # -> X_1[2] = X[2] - X[1] = 21 - 9
X_2 = [6, 9, 6]  # -> X_2[2] = X_1[2] - X_1[0] = 12 - 6
X_3 = [6, 3, 6]  # -> X_3[1] = X_2[1] - X_2[0] = 9 - 6
X_4 = [6, 3, 3]  # -> X_4[2] = X_3[2] - X_3[1] = 6 - 3
X_5 = [3, 3, 3]  # -> X_5[1] = X_4[0] - X_4[1] = 6 - 3

"""

import math
from functools import reduce

def solution(lst):
    gcd = reduce(math.gcd,lst)
    return gcd * len(lst)

#Other solution:
import numpy as np

def solution(a):
    return np.gcd.reduce(a) * len(a)


# Example usage:
if __name__ == "__main__":
    print(solution([6, 9, 21]))  # Output: 9
    print(solution([5, 10, 15]))  # Output: 15
    print(solution([7, 14, 28]))  # Output: 21