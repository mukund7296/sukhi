class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


p1 = Person("John", 36)
p2 = Person("Mukund", 34)
p1.name="Taapse"

print(p1.name,p1.age)

print(p2.name,p2.age)

import re

#Return a list containing every occurrence of "ai":

str = "The rain in Spain"
x = re.findall("ai", str)
print(x)
