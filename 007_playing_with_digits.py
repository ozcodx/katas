"""
Given two positive integers n and p, we want to find a positive integer k, if it
exists, such that the sum of the digits of n raised to consecutive powers
starting from p is equal to k * n. 
"""

def dig_pow(n, p):
    sum = 0
    for d in str(n):
        sum += int(d) ** p
        p += 1
    if sum % n == 0:
        return sum / n
    else:
        return -1