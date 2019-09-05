"""23.Write a Python program to accept a filename from the user and print the extension of that.

Program:
"""
filename=input("input the file name : -")

ext=filename.split(".")

print("The extension of the file is : "+repr(ext[-1]))