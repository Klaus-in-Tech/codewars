"""
In this kata you have to create a domain name validator mostly compliant with RFC 1035, RFC 1123, and RFC 2181

For purposes of this kata, following rules apply:

Domain name may contain subdomains (levels), hierarchically separated by . (period) character
Domain name must not contain more than 127 levels, including top level (TLD)
Domain name must not be longer than 253 characters (RFC specifies 255, but 2 characters are reserved for trailing dot and null character for root level)
Level names must be composed out of lowercase and uppercase ASCII letters, digits and - (minus sign) character
Level names must not start or end with - (minus sign) character
Level names must not be longer than 63 characters
Top level (TLD) must not be fully numerical
Additionally, in this kata

Domain name must contain at least one subdomain (level) apart from TLD
Top level validation must be naive - ie. TLDs nonexistent in IANA register are still considered valid as long as they adhere to the rules given above.
The validation function accepts string with the full domain name and returns boolean value indicating whether the domain name is valid or not.
"""

import re


def validate(domain):
    if not domain or len(domain)>253:
        return False
    levels = domain.split(".")
    
    if len(levels)<2 or len(levels)> 127:
        return False

    level_pattern = re.compile(r'^[a-zA-Z0-9-]+$')
    for level in levels:
        if not level:
            return False
        if len(level)>63:
            return False
        if level.startswith("-") or level.endswith("-"):
            return False
        if not level_pattern.fullmatch(level):
            return False
    tld = levels[-1]
    if tld.isdigit():
        return False
    return True

#Other Solutions
import re


def validate(domain):
    return re.match('''
        (?=^.{,253}$)          # max. length 253 chars
        (?!^.+\.\d+$)          # TLD is not fully numerical
        (?=^[^-.].+[^-.]$)     # doesn't start/end with '-' or '.'
        (?!^.+(\.-|-\.).+$)    # levels don't start/end with '-'
        (?:[a-z\d-]            # uses only allowed chars
        {1,63}(\.|$))          # max. level length 63 chars
        {2,127}                # max. 127 levels
        ''', domain, re.X | re.I)

#Test cases
validate("example.com")  # True
validate("sub.example.com")  # True
validate("sub-domain.example.com")  # True
validate("sub-domain.example.co.uk")  # True
