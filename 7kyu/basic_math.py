"""
In this kata, you will do addition and subtraction on a given string. The return value must be also a string.

Note: the input will not be empty.

Examples
"1plus2plus3plus4"  --> "10"
"1plus2plus3minus4" -->  "2"
"""

def calculate(s):
    # Replace 'plus' and 'minus' with '+' and '-'
    expr = s.replace('plus', '+').replace('minus', '-')
    # Evaluate the expression and return as string
    return str(eval(expr))

# Other solutions
def calculate(s):
    s = s.replace('minus',' -')
    s = s.replace('plus',' ')
    s = s.split(' ')
    s = str( sum( [(int(x)) for x in s] ) )
    return s