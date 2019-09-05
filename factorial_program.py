"""12.Program to find factorial of a number using recursion
"""


def fact1(n):
    if n==0:
        return 1
    else:
        result=n*fact1(n-1)
        return result
n = int(input("Enter a value to find fact : "))
print("fact of is:",fact1(n))