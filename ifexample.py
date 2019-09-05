a = 200
b = 200
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))