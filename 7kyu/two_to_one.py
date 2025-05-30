"""
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string (alphabetical ascending), the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

"""

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

# Other solutions
def longest(s1, s2):
    # Combine the two strings and convert to a set to remove duplicates
    combined = set(s1 + s2)
    # Sort the characters and join them into a string
    return ''.join(sorted(combined))