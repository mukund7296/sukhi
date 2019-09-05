"""39:-Write a Python program to get the least common multiple (LCM) of two positive integers.
"""
import math
def lcm(a, b):
    return abs(a*b)      // math.gcd(a, b)

v1=lcm(4,6)
print(v1)