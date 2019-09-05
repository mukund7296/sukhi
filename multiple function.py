"""7.Write a program to  retrun multiple values from functions

program:
"""

def multiple_function(x,y):
    addition=x+y
    subtraction=x-y
    multiply = x*y
    divide = x/y
    mod=x%y
    power=x**y
    return addition,subtraction,multiply,divide,mod,power

a,b,c,d,e,f=multiple_function(12,10)
print("addition :\t",a,"\nSubtraction : \t",b,"\nMultiplication \t",c,"\nDivision \t",d,"\nMod\t",e,"\nPower of Number are\t",f)