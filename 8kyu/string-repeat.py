"""
Write a function that accepts a non-negative integer n and a string s as parameters, and returns a string of s repeated exactly n times.

Examples (input -> output)
6, "I"     -> "IIIIII"5, "Hello" -> "HelloHelloHelloHelloHello"
"""

def repeat_str(repeat, string):
    res = ''
    for _ in range(repeat):
        res+=string
    return res