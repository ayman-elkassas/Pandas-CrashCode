import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(654546465)

df=pd.DataFrame(
    [
        [15,32,101],
        [np.NaN,64,103],
        [np.NaN,52,np.NaN],
    ],
    index=['A','B','C'],
    columns = ['C1','C2','C3']
)

# print(df)

# drop any row exist cell with NaN by default axis=0
# threshold is number of min number of nan
df_wn=df.dropna(axis=1,thresh=2)

print(df_wn)

print(df.filter(like='B', axis=0))

df.fillna(555)