#collection of data types
#List, tuple, set, frozen set, dictnary, bytearray, range , bytes

# 1> List concept represented by square bracket [ ]
# duplicates are allowed
L1=[10,"Mukund",20,"Hansraj",30,"Anand",0b1111,0xface,0o123,True,False,12.00]
print(L1)
print(type(L1))
L2=[2]
L2[0]=2223423423
L2.append(100)
L2.extend(L1)
print(type(L2))
print(L2)

