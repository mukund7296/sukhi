# char data types is not availables we represent with str data type
a=10
b=10
c=20
print(id(a),id(b),id(c))

#int   to convert from any other types to int type.
cc=20.999
print(int(cc))
#after dot values will be gone
dd=10.9909
print(int(dd))

#float

cc=20
print(float(cc))
#bool
ddd=True
print(int(ddd))
ddd=False
print(int(ddd))

#Complex
vv=10+20j
"""
print(int(vv))
20
10
TypeError: can't convert complex to int
"""


#string Str
cc=int(0B1111)
print(cc)
