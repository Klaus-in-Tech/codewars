"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def solution(s):
    result = []
    for char in s:
        if char.isupper():
            result.append(' ')
        result.append(char)
    return ''.join(result)

#Other Solutions
def solution(s):
    """
    Breaks camel case strings into separate words by inserting spaces before uppercase letters.
    
    Args:
    s (str): The input string in camel case format.
    
    Returns:
    str: The modified string with spaces inserted before uppercase letters.
    """
    return ''.join([' ' + char if char.isupper() else char for char in s]).lstrip()