"""
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
"""

def alphabet_position(text):
    dict_alphanum = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,
                    'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    num_sentence = []
    for  char in text.lower():
        if char.isalpha():
            num_sentence.append(dict_alphanum[char])
    return ' '.join(str(num) for num in num_sentence)

#Other Solutions
from string import ascii_lowercase


def alphabet_position(text):
    return ' '.join(str(ascii_lowercase.index(n.lower()) + 1) for n in text if n.isalpha())