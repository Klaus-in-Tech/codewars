from collections import Counter

def first_non_repeating_letter(s: str) -> str:
    """
    Return the first character in s that does not repeat (case-insensitive),
    preserving the original case. Returns empty string if none found.
    """
    if not s:
        return ""
    string_lower = [ch.lower() for ch in s]
    counts = Counter(string_lower)
    for orig, f in zip(s, string_lower):
        if counts[f] == 1:
            return orig
    return ""


#Other solution
def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
            
    return ""

if __name__ == "__main__":
    # Example usage
    print(first_non_repeating_letter("sTreSS"))  # Output: "T"
    print(first_non_repeating_letter("aabbcc"))  # Output: ""
    print(first_non_repeating_letter("moonmen"))         # Output: ""  
    print(first_non_repeating_letter("~><#~><"))  # Output: ","
    