"""
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
"""

def fake_bin(x):
    res = ''
    # Traversing through integers in the string
    for c in x:
        if int(c) <5:
            res = res + '0'
        else:
            res = res + '1'
    return res

# Other solutions
def fake_bin(x):
    # Use a list comprehension to replace digits and join them into a string
    return ''.join(['0' if int(c) < 5 else '1' for c in x])