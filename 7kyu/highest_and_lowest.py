"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""

#Input string of numbers
#Output 

def high_and_low(numbers):
    # ...
    str_nums = numbers.split(" ")
    nums = [int(num) for num in str_nums]
    max_num = max(nums)
    min_num = min(nums)
    return f'{max_num} {min_num}'

# Other solutions
def high_and_low(numbers):
    # Split the input string into a list of numbers
    nums = list(map(int, numbers.split()))
    # Find the maximum and minimum numbers
    return f"{max(nums)} {min(nums)}"