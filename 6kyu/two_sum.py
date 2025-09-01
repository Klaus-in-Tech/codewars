"""
Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indexes of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Based on: https://leetcode.com/problems/two-sum/
"""



import itertools

def two_sum(numbers, target):
    ...
    combs = itertools.combinations(numbers,2)
    for comb in combs:
        if sum(comb) == target and comb[0] != comb[1]:
            return (numbers.index(comb[0]),numbers.index(comb[1]))


#Other Solutions
def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]