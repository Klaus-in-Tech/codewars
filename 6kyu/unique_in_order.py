""""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""

def unique_in_order(sequence):
    if not sequence:
        return []
    
    result = [sequence[0]]
    for item in sequence[1:]:
        if item != result[-1]:
            result.append(item)
    return result


# Test cases
print(unique_in_order('AAAABBBCCDAABBB'))  # Output: ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order('ABBCcAD'))          # Output: ['A', 'B', 'C', 'A', 'D']
print(unique_in_order([1, 2, 2, 3, 3]))          # Output: [1, 2, 3]
print(unique_in_order([]))                     # Output: []
print(unique_in_order('A'))                    # Output: ['A']
print(unique_in_order('AA'))                   # Output: ['A']