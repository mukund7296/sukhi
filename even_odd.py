'''4.Write a python program to print given number is even or odd.

Program:
'''
def num(a):
    if a%2==0:
        print("given nm is even")
    else:
        print("give num is odd")

var1=int(input("Enter your number for odd or even :- "))
var=num(var1)
print(var)
