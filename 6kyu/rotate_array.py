"""
Create a function named "rotate" that takes an array and returns a new one with the elements inside rotated n spaces.

If n is greater than 0 it should rotate the array to the right. If n is less than 0 it should rotate the array to the left. If n is 0, then it should return the array unchanged.

Example:

data = [1, 2, 3, 4, 5];

rotate(data, 1) # => [5, 1, 2, 3, 4]
rotate(data, 2) # => [4, 5, 1, 2, 3]
rotate(data, 3) # => [3, 4, 5, 1, 2]
rotate(data, 4) # => [2, 3, 4, 5, 1]
rotate(data, 5) # => [1, 2, 3, 4, 5]

rotate(data, 0) # => [1, 2, 3, 4, 5]

rotate(data, -1) # => [2, 3, 4, 5, 1]
rotate(data, -2) # => [3, 4, 5, 1, 2]
rotate(data, -3) # => [4, 5, 1, 2, 3]
rotate(data, -4) # => [5, 1, 2, 3, 4]
rotate(data, -5) # => [1, 2, 3, 4, 5]
Furthermore the method should take ANY array of objects and perform this operation on them:

rotate(['a', 'b', 'c'], 1)     # => ['c', 'a', 'b']
rotate([1.0, 2.0, 3.0], 1)     # => [3.0, 1.0, 2.0]
rotate([True, True, False], 1) # => [False, True, True]
Finally the rotation shouldn't be limited by the indices available in the array. Meaning that if we exceed the indices of the array it keeps rotating.

Example:

data = [1, 2, 3, 4, 5]

rotate(data, 7)     # => [4, 5, 1, 2, 3]
rotate(data, 11)    # => [5, 1, 2, 3, 4]
rotate(data, 12478) # => [3, 4, 5, 1, 2]
"""


def rotate(arr, n):
    if not arr or n == 0:
        return arr[:]
    length = len(arr)
    n = n % length  # Normalize n to array length
    return arr[-n:] + arr[:-n] if n else arr[:]

#Other Solutions
from collections import deque


def rotate(arr, n):
    """Return a given array, rotated by n spaces."""
    rotator = deque(arr)
    rotator.rotate(n)
    return list(rotator)


# Examples:
# data = [1, 2, 3, 4, 5]
# print(rotate(data, 1))  # [5, 1, 2, 3, 4]
# print(rotate(data, -1)) # [2, 3, 4, 5, 1]
# print(rotate(data, 7))  # [4, 5, 1, 2, 3]