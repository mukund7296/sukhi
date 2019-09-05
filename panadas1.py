import pandas as pd
ds=pd.Series([9911,222,333,224,533,6444])
print(ds)

ds = pd.Series([2, 4, 6, 8, 10])
print("Pandas Series and type")
print(ds)
print(type(ds))
print("Convert Pandas Series to Python list")
print(ds.tolist())
print(type(ds.tolist()))