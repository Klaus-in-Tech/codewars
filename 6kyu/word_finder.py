"""
In this kata you have to extend the dictionary with a method, that returns a list of words matching a pattern. This pattern may contain letters (lowercase) and placeholders ("?"). A placeholder stands for exactly one arbitrary letter.

Example:

var fruits = new Dictionary(['banana', 'apple', 'papaya', 'cherry']);
fruits.getMatchingWords('lemon');     // must return []
fruits.getMatchingWords('cherr??');   // must return []
fruits.getMatchingWords('?a?a?a');    // must return ['banana', 'papaya']
fruits.getMatchingWords('??????');    // must return ['banana', 'papaya', 'cherry']
Additional Notes:

the words and patterns are all lowercase
the order of the returned words doesn't matter
"""

class Dictionary: 
    def __init__(self, words):
        self.words = words
        
    def get_matching_words(self, pattern):
        # your code here
        matches = []
        for word in self.words:
            if len(word) != len(pattern):
                continue
            match = True
            for i in range(len(pattern)):
                if pattern[i] != '?' and pattern[i] != word[i]:
                    match = False
                    break
            if match:
                matches.append(word)
        return matches
    


#Other solutions:
import re

class Dictionary: 
    def __init__(self, words):
        self.words = words
        
    def get_matching_words(self, pattern):
        # your code here
        return [word for word in self.words if re.fullmatch(pattern.replace('?', '.'), word )]

    
fruits = Dictionary(['banana', 'apple', 'papaya', 'cherry'])
print(fruits.get_matching_words('lemon'))     # []
print(fruits.get_matching_words('cherr??'))   # []
print(fruits.get_matching_words('?a?a?a'))    # ['banana', 'papaya']
print(fruits.get_matching_words('??????'))    # ['banana', 'papaya', 'cherry']