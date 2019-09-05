import copy

L1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Before List 1 values are :-",L1)
L2=copy.copy(L1)
print("Before List 2 values are :-",L2)
L2.append("A")
L2.append("B")
L2.append("C")
print("After List 2 values are :-",L2)
print("After List 1 values are :-",L1)

L3=copy.deepcopy(L1)

print(L3)
L3.append("Mukund")
L3.append("Hansraj")
print("Before List 1 values are :-",L1)
print(L3)
print("Before List 1 values are :-",L1)
