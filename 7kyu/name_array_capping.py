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