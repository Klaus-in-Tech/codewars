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