"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false

"""

import re

def validate_pin(pin):
    # return true or false
    pattern = r"^\d{4}$|^\d{6}$"
    pin_code = re.fullmatch(pattern,pin)
    return bool(pin_code)

# Other solutions
def validate_pin(pin):
    # Check if the pin is a string of digits and has a length of 4 or 6
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)