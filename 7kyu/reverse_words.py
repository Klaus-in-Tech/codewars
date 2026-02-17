"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""

def reverse_words(text):
    reversed_words = []
    for word in text.split(" "):
        reversed_words.append(word[::-1])
    return " ".join(reversed_words)

# Other solutions
def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))

# 17th-02-2026 Other solution
def reverse_words(text):    
    splitted_words_from_text = text.split(" ")
    reversed_words_in_an_array = [word[::-1] for word in splitted_words_from_text]
    return " ".join(reversed_words_in_an_array)