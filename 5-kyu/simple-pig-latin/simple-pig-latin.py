import re
def pig_it(text):
    #your code here
    res = []
    for word in text.split(" "):
        if re.fullmatch(r'[A-Za-z]+',word):
            res.append(word[1:]+word[0]+"ay")
        else:
            res.append(word)
    return " ".join(res)