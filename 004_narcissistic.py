import math

"""
The code return true or false (not 'true' and 'false') depending upon whether
the given number is a Narcissistic number in base 10. 
A Narcissistic Number (or Armstrong Number) is a positive number which is the
sum of its own digits, each raised to the power of the number of digits
"""

def narcissistic( num ):
    string = str(num)
    num_digits = len(string)
    sum = 0
    for char in string:
        digit = int(char)
        sum += digit ** num_digits
    return bool(num == sum)