import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(654546465)

df=pd.DataFrame(
    randn(5,3),
    index=['A','B','C','D','E'],
    columns=['C1','C2','C3']
)

# select rows
print(df.head(2))

op=df<=0

print(df[op])

print(' ')
print('Filtered DataFrame')
# select all rows that value of C3 <=0
op2=(df['C3']<=0) | (df['C1']>=0.1)
df_after_filter=df[op2]

print(df_after_filter['C1'])