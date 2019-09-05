"""11.Program to declare a global variable
"""
#global variable
a=10
b=20
c=90
def fun1():
    print("Global variable",a)
    print("Global variable",b)

def fun2():
    global c  # globle variable called in local
    a=30    # Local variable
    b=40    #local variable
    print("Local Variable ",a)
    print("Local Variable ",b)
    print("Global variable called in local",c)

fun1()

fun2()