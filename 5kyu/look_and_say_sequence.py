"""
In mathematics, the look-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, 312211, …
To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit. For example:

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
1211 is read off as "one 1, then one 2, then two 1s" or 111221.
111221 is read off as "three 1s, then two 2s, then one 1" or 312211.
Your mission is to write a function which, given an integer n as parameter, returns a comma separated list of the first n terms of the sequence. For 0, an empty string shall be returned.

Examples
2  -->  "1,11"
3  --> "1,11,21"
5  --> "1,11,21,1211,111221"
"""

def look_and_say_sequence(n):
    if n == 0:
        return ""
    sequence = ["1"]
    for _ in range(1, n):
        current_term = sequence[-1]
        next_term = ""
        count = 1
        for j in range(1, len(current_term)):
            if current_term[j] == current_term[j-1]:
                count += 1
            else:
                next_term += str(count) + current_term[j-1]
                count = 1
        next_term += str(count) + current_term[-1]
        sequence.append(next_term)
    return ",".join(sequence)




# Example usage:

print(look_and_say_sequence(3))  # Output: "1,11,21"
print(look_and_say_sequence(1))  # Output: "1"
print(look_and_say_sequence(2))  # Output: "1,11"
print(look_and_say_sequence(5))  # Output: "1,11,21,1211,111221"
print(look_and_say_sequence(0))  # Output: ""

