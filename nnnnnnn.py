"""26:Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

Program:
"""
a=int(input("input an integer:"))

n1=int("%s"%a)

n2=int("%s%s"%(a,a))

n3=int("%s%s%s"%(a,a,a))

n4=int("%s%s%s%s"%(a,a,a,a))

n5=int("%s%s%s%s%s"%(a,a,a,a,a))

print(n1+n2+n3+n4+n5)

"""27.Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

Program:
"""
print(abs.__doc__)

"""28:.Write a Python program to print the calendar of a given month and year

Program:
"""
import calendar

y=int(input("input the year:"))

m=int(input("input the month :"))

print(calendar.month(y,m))

