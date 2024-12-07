'''
Check to see if a string has the same amount of 'x's and 'o's. The method must
return a boolean and be case insensitive. The string can contain any char.
'''

def xo(s):
    s = s.lower()
    x = s.count('x')
    o = s.count('o')
    return x == o