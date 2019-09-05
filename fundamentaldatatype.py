#mutable means changable and immutable is non-changable
'''
x=10
#x is reference variable and 10 is value
print(x)
print(id(x))
x=10
print(x)
print(id(x))
x=10+1
print(x)
print(id(x))
'''
a=[1,2,3,4,5,6,7]
print(id(a))
print((a))
a.append(11)
a.pop()
a.reverse()
print((a))
print(id(a))