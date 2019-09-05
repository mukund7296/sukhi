"""22.Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

Program:
"""
values=input("input of some numbers separated with commmas:").split(",")

tuple=tuple(values)
set=set(values)
frozenset=frozenset(values)

print("List Values are :-",values)

print("Tuple values are :-",tuple)
print("Set values are :-",set)
print("frozenset values are :-",frozenset)