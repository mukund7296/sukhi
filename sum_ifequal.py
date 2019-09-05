"""40:-Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

Program:
"""
def sum(x,y,z):
    if x==y or y==z or x==z:
        sum=0
    else:
        sum=x+y+z
    return sum

print(sum(2,4,4))

print(sum(4,5,6))

print(sum(5,5,5))

print(sum(7,8,9))