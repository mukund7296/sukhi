"""29:- Write a Python program to calculate number of days between two dates.

Program:from datetime import date
"""
from datetime import date
fdate=date(2018,3,21)

ldate=date(2019,3,30)

days=ldate-fdate

print("No of days are :-",days.days)