"""
If a singular noun ends in '-s', '-x', '-z', '-ch' or '-sh', add '-es'

If a singular noun ends with a consonant and '-y', change '-y' to '-ies'.

All other words just add '-s'

None of the tests end in '-f' or '-o' and none are irregular nouns (e.g. child, mouse etc.)

Examples

table -> tables,
window -> windows,
church -> churches,
watch -> watches,
bus -> buses,
box -> boxes,
buzz -> buzzes,
fly -> flies
"""


def pluralize(word):
    if  word.endswith("s") or word.endswith("x") or word.endswith("z") or word.endswith("ch") or word.endswith("sh"):
        return word+"es"
    elif word.endswith("y") and word[-2] not in 'aeiou':
        return word[:-1]+"ies"
    else:
        return word+"s"
    
# Other solutions
def pluralize(word):
    return word + ("es" if word.endswith(("s", "x", "z", "ch", "sh")) else "ies" if word.endswith("y") and word[-2] not in 'aeiou' else "s")