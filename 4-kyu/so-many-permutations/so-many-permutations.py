from itertools import permutations as perm
​
def permutations(s):
    # Code Away!
    all_permutations = perm(s)
    output = [''.join(item) for item in all_permutations]
    return list(set(output))