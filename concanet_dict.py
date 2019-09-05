"""15.Write a Python program to concatenate following dictionaries to create a new one.
"""
dic1={"Apple":10, "Banana":20}

dic2={"Orange":30, "staberry":40}

dic3={"tomato":50,"potato":60}

dic4 = {}

for d in (dic1, dic2, dic3):
    dic4.update(d)

print(dic4)