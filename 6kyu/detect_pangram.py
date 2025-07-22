"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.


"""

import re

def is_pangram(st):
        letters = set()
        for c in st.lower():
            if re.match('^[a-z]+$',c):
                letters.add(c)
            if len(letters) == 26:
                return True
        return False


#Other Solution
import string

def is_pangram(s):
    return all(i in s.lower() for i in string.ascii_lowercase)