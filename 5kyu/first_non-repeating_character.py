"""
Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");

† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.
"""

from collections import Counter

def first_non_repeating_letter(s: str) -> str:
    """
    Return the first character in s that does not repeat (case-insensitive),
    preserving the original case. Returns empty string if none found.
    """
    if not s:
        return ""
    string_lower = [ch.lower() for ch in s]
    counts = Counter(string_lower)
    for orig, f in zip(s, string_lower):
        if counts[f] == 1:
            return orig
    return ""


#Other solution
def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
            
    return ""

if __name__ == "__main__":
    # Example usage
    print(first_non_repeating_letter("sTreSS"))  # Output: "T"
    print(first_non_repeating_letter("aabbcc"))  # Output: ""
    print(first_non_repeating_letter("moonmen")) # Output: ""  
    print(first_non_repeating_letter("~><#~><")) # Output: "#"
    