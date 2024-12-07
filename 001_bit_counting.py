# Hamming weight

'''
Write a function that takes an integer as input, and returns the number of 
bits that are equal to one in the binary representation of that number. 
You can guarantee that input is non-negative.
'''

# Bitwise operations, the and with the previous number remove the 
# least significant bit that is one.

def count_bits(n):
    c = 0
    while n != 0:
        c += 1
        n = n & (n-1)
    return c

# int.bit_count(n)