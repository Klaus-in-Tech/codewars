"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.


"""

def accum(st):
    #The first letter is capitalised 
     converted_string = list(st)
     mumbled_list = []
     for index,char in enumerate(converted_string):
           mumbled_list.append(char*(index+1))

     mumbled_list = [c.title() for c in mumbled_list]
    
     return "-".join(mumbled_list)

# Other solutions
def accum(st):
    return '-'.join((c * (i + 1)).capitalize() for i, c in enumerate(st))