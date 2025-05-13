#Input is an array of string
#Ouput: Print a single character separated with a

def print_array(arr):
    #Checking if it is a single element in the array
    if len(arr)<2:
        return str(arr[0])
    # Traversing through integers in the array
    for i in arr:
        return ",".join(str(i) for i in arr)

    
    # Traversing through characters in array
    for c in arr:
        if isinstance(c,str):
            return ",".join(arr)       
            pass


#Other solutions
def print_array(arr):
    # Convert all elements to strings and join them with commas
    return ",".join(str(element) for element in arr)

# Example usage:
print(print_array(["h", "o", "l", "a"]))  # Output: "h,o,l,a"