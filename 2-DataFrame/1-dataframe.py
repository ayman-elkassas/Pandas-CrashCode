# dataframe like table
import pandas as pd

# DataFrame(values,index of rows -> determine num of rows,columns title)

# if you want to initialize all cells of data frame with zero put 0 in values

df1=pd.DataFrame(0,index=['X1','X2','X3'],columns=['C1','C2'])

print(df1)

# if you want to index as numerical and shift it as
df2=df1.reset_index()
print(df2)