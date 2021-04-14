import pandas as pd

headers=['name','age','weight']
values=['ahmed',25,64]

# series the same of dictionary in python

series1=pd.Series(index=headers,data=values)
# index is keys, data is values

print(series1)

# if does not put index by default numeric from 0 to length of values
series2=pd.Series(values)

print(series2)

# values can be any object and may be function
series3=pd.Series([str,print])
print(series3)
