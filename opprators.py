"""Python Operators

Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators
"""
thislist = ["Apple", "banana", "cherry"]
print(thislist)
print(thislist[1])
print(thislist[2][::-1])

if "Apple" in thislist:
    print("This fruit is available ")
else:
    print("No ")


thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


lisst=[1,2,3,4,5,6]
print(type(lisst))


lisst=(1,2,3,4,"mukund",5,6)
print(type(lisst))
print(lisst)


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])