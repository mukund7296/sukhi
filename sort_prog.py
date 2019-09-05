"""13.Write a Python program to sort (ascending and descending) a dictionary by value.
"""
import operator

d = {1: 12, 3: 14, 4: 3, 2: 1, 0: 0}

print('Original dictionary : ',d)

sorted_d = sorted(d.values())

print("Dictionary in ascending order by value : ",sorted_d)

sorted_d = sorted(d.values(),reverse=True)

print("Dictionary in descending order by value : ",sorted_d)