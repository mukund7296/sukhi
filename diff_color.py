"""38: Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2

Program:
"""
l1=set(["White","Black","Red"])

l2=set(["White","Black","Yellow"])

print(l1.difference(l2))

print(l2.difference(l1))

"""38 :- Write a Python program that will accept the base and height of a triangle and compute the area.

program:
"""
b=int(input("Enter the base of a triangle :"))

h=int(input("Enter the height of a triangle :"))

area=1/2 * b * h

print("Area is :",area)