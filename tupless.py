# 2> Tuples is concept represnted by () parantheses
#duplicates are allowed
#its immutables and read only version
L2=(1,2,3,4,5,8,1,2,3,4,5,8,"Mukund")
print(L2)
print(type(L2))
print(L2[-1])

L2=(10,)
print(type(L2))
#integer show
L2=(10)
print(type(L2))

#3> duplicates are not allowed ,order not allowed
#if i want to send one message to customer for offer then better for go to set .duplicate mobile not allowed
s1={1,2,3,4,5,6,6,3,3,2,2,1,7}

print(s1)
s1.add(1000)
print(s1)
print(type(s1))
s2=frozenset(s1)
print(type(s2))

dd={}
dd[0]="Mukund"
dd[2]="Rajesh"
dd[0]="girish"
dd[2]="Rajesh"
print(dd)