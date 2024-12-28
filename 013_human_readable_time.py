"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)s
"""


def make_readable(seconds):
    seg = seconds % 60
    min = seconds // 60
    hor = min // 60
    min = min % 60
    return '{:02}'.format(hor) + ":" + '{:02}'.format(min) + ":" + '{:02}'.format(seg)