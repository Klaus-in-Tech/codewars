"""
In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

Examples:

With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
Note: The order of the permutations doesn't matter.

Good luck!


"""

import itertools

def permutations(s):
    all_permutations = itertools.permutations(s)
    list_permutations = ["".join(p) for p in all_permutations]
    return set(list_permutations)

# Example usage:
print(permutations('aabb'))
