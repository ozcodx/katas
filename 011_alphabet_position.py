"""
In this kata you are required to, given a string, replace every letter with its
position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
"""

def alphabet_position(text):
    lets = []
    for char in text.lower():
        num = ord(char) - 96
        if num > 0 and num <= 26:
            lets.append(num)
    return " ".join(str(n) for n in lets) 