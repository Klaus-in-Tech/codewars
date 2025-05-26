"""
Create a function that accepts an array of names, and returns an array of each name with its first letter capitalized and the remainder in lowercase.

Examples
["jo", "nelson", "jurie"] -->  ["Jo", "Nelson", "Jurie"]
["KARLY", "DANIEL", "KELSEY"] --> ["Karly", "Daniel", "Kelsey"]

"""


def cap_me(arr):
    capitalized_arr = []
    for name in arr:
        capital_name = name.title()
        capitalized_arr.append(capital_name)
    return capitalized_arr


# Other solutions
def cap_me(arr):
    # Use a list comprehension to capitalize each name in the array
    return [name.title() for name in arr]