"""47:-Write a Python program to parse a string to Float or Integer.

Solution:-
"""
n ="246.2458"

print(float(n))

print(int(float(n)))

"""48 : Write a Python program to print without newline or space?

Solution:-
"""
for i in range(0, 10):

    print("*"* i)

print("\n")
"""49: Write a Python program to get the current username
"""
import getpass

print(getpass.getuser())