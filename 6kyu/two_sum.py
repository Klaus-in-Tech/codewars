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
            

def two_sum(nums,target):
    dict = {}
    for i,_first_num in enumerate(nums):
        _second_num = target - _first_num
        if _second_num in dict:
            return (dict[_second_num],i)
        dict[_first_num] = i
        

if __name__ == "__main__":
    print(two_sum([1, 2, 3], 4) )