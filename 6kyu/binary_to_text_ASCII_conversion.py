"""
Write a function that takes in a binary string and returns the equivalent decoded text (the text is ASCII encoded).

Each 8 bits on the binary string represent 1 character on the ASCII table.

The input string will always be a valid binary string.

Characters can be in the range from "00000000" to "11111111" (inclusive)

Note: In the case of an empty binary string your function should return an empty string.
"""


def binary_to_string(binary):
     
    if not binary:
        return ''
    # Creating the chunks 
    chunks = [binary[i:i+8] for i in range(0,len(binary),8)]
    # Converting binary to demical and demical to ASCII characters
    text = ''.join([chr(int(chunk,2)) for chunk in chunks])
    return text

#Other Solutions:
def binary_to_string(binary):
    if not binary:
        return ''
    return ''.join([chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)])

# Example usage:
print(binary_to_string("0100100001100101011011000110110001101111"))  # Output: "Hello"
