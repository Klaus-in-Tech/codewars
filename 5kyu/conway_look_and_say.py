"""
Your task is to create a function that will take an integer and return the result of the look-and-say function on that integer. This should be a general function that takes as input any positive integer, and returns an integer; inputs are not limited to the sequence which starts with "1".

Conway's Look-and-say sequence goes like this:

Start with a number.
Look at the number, and group consecutive digits together.
For each digit group, say the number of digits, then the digit itself.
This can be repeated on its result to generate the sequence.

For example:

Start with 1.
There is one 1 --> 11
Start with 11. There are two 1 digits --> 21
Start with 21. There is one 2 and one 1 --> 1211
Start with 1211. There is one 1, one 2, and two 1s --> 111221
Sample inputs and outputs::

0 --> 10
2014 --> 12101114
9000 --> 1930
22322 --> 221322
222222222222 --> 122

"""

def look_and_say(n: int) -> int:
    """Return the look-and-say transform of a non-negative integer n."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    s = str(n)
    out_parts = []
    prev = s[0]
    count = 1
    for ch in s[1:]:
        if ch == prev:
            count += 1
        else:
            out_parts.append(str(count))
            out_parts.append(prev)
            prev = ch
            count = 1
    out_parts.append(str(count))
    out_parts.append(prev)
    return int("".join(out_parts))



#other solution:    
from itertools import groupby

def look_say(n):
    return int("".join(f'{len(list(v))}{k}' for k, v in groupby(str(n))))

# Example usage:
if __name__ == "__main__":
    print(look_and_say(1))      # Output: 11
    print(look_and_say(11))     # Output: 21
    print(look_and_say(21))     # Output: 1211
    print(look_and_say(1211))   # Output: 111221
    print(look_and_say(111221)) # Output: 312211