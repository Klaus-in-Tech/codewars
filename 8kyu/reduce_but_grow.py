""""
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
"""

# Input an array of positive integers
# Output product of all the integers in the array in order

def grow(arr):
    result = 1
    for i in arr:
        result *= i
    return result

# Other solutions
def grow(arr):
    # Use the built-in function reduce to multiply all elements in the array
    from functools import reduce
    return reduce(lambda x, y: x * y, arr)