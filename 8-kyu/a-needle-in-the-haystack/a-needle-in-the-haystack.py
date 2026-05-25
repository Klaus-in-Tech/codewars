def find_needle(haystack):
    # your code here
    for index,item in enumerate(haystack):
        if item == "needle":
            return f"found the needle at position {index}"