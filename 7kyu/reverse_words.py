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