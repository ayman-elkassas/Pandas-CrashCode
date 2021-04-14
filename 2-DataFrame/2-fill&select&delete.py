import numpy as np
import pandas as pd
from numpy.random import randn

# if you want to every time run code random values does not change
np.random.seed(105545454)

df=pd.DataFrame(randn(3,3),index=['X','Y','Z'],columns=['C1','C2','C3'])

print(df)

# fetch one column
# df['C1']

# fetch multi columns
# df[ ['C1','C3'] ]

# print(df[ ['C1','C3'] ])

# sum two column
df['C4']=df['C1']+df['C2']

# print(df)

# select rows
print(df.loc['Y'])

# select rows with index 0,1,...
print(df.iloc[1])

# select multi rows
print(df.loc[['X','Z'],['C1','C2']])

# select cell
print(df.loc['X','C1'])

# to delete row or column , and replace
df.drop(['C4','C3'],axis=1,inplace=True)

print(df)