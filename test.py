x=10
y=x
print(id(x))
print(id(y))
y=y+5
print(id(y))
print(id(x))
# One object is created and 3 reference variables are pointing to variable is created
a=10
b=10
c=10
print(id(a))
print(id(b))
print(id(c))

a="ryan"
b="ryan"
print(id(a))
print(id(b))
print(a is b)