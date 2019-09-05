var=range(100,10,-2)
for i in var:
    print(i)
print(type(var))
'''
for y in range(1,100,2):
    print(y)
for n in range(-20,0):
    print(n)

'''

var=[2,3,4,222,255]
print(bytes(var))


#bytearray we use for binary data to store video audio etc
var1=[2,3,4,222,255]
print(bytearray(var1))
var1.append(2333)
print(var1)

#non data type

def f1():
    print("Hello")
x=f1()
print(x)

#None output getting None

