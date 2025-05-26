"""
Find the sum of the odd numbers within an array, after cubing the initial integers. The function should return undefined/None/nil/NULL if any of the values aren't numbers.

Note: Booleans should not be considered as numbers.


"""

def cube_odd(arr):

    #Identifying non integer values within an array 
    for i in arr:
        if (not isinstance(i,int)):
            return None
    #Identifying boolean values within an array
    for i in arr:
        if isinstance(i, bool):
            return None
    #Identifying the odd numbers with an array
    odd_arr = []
    for i in arr:
        if i%2 != 0:
            odd_arr.append(i)
    cube_arr =[i**3 for i in odd_arr]
    return sum(cube_arr)
        
#Other solutions
def cube_odd(arr):
    # Check if all elements are numbers
    if not all(isinstance(i, (int, float)) for i in arr):
        return None

    # Calculate the sum of cubes of odd numbers
    return sum(i ** 3 for i in arr if isinstance(i, int) and i % 2 != 0)    
 