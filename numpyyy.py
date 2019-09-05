import numpy as np
a=np.array([1,2,3])    # 1 D array
print(a)
b=np.array([[1,2,3],[4,5,6]])  # 2 D array
print(b)

c=np.ones((5,5))
print(c)
import pandas as pd
l1=[1,2,3,4,5]
data1=pd.DataFrame(l1)
print(data1)

dd1={"fruit_names":["apple","banana","staberry","guhava","cherry"],"Vegitables":["Chilli","Tomato","Potato","pudina","onion"]}
dd2=pd.DataFrame(dd1)
print(dd2)

