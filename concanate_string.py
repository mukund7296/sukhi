"""52:Write a Python program to concatenate N strings.

Program:
"""
list_of_colors=['red',"White",'Black']

colors='-'.join(list_of_colors)

print()

print("all colors:"+colors)

print()


def fact(x):
    if x==0:
        return 1
    else:
        result=x*fact(x-1)
        return result
v=fact(5)
print(v)