"""
sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
"""

import re
def order(sentence):
    r = {}
    for s in sentence.split():
        n = re.sub('\D', '', s)
        r[n]=s
    return " ".join(dict(sorted(r.items())).values())
