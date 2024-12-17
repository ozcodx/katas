"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5
below the number passed in.

Additionally, if the number is negative, return 0.
"""

def solution(number):
    s3 = range(3,number,3)
    s5 = range(5,number,5)
    s = set(list(s3)+list(s5))
    return sum(s)