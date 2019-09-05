"""45:-Write a Python program to check whether a file exists.

Solution:-
"""
import os.path

open("abc.txt","w")

print(os.path.isfile("abc.txt"))
"""46:-Write a Python program to find out the number of CPUs using.

Solution:-
"""
import multiprocessing

print(multiprocessing.cpu_count())