"""Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:

case	return
name equals owner	'Hello boss'
otherwise	'Hello guest'

"""

# Input string of name 
# Output string 

def greet(name, owner):
    # Add code here
    if(name == owner):
        return 'Hello boss'
    
    return 'Hello guest'

#Other solution
def greet(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'