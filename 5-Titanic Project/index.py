import pandas as pd
import matplotlib.pyplot as plt

# for excel there is xlrd dep on this operation
df=pd.read_excel('titanic.xls')

# todo:info

# print(df.head(10))
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())

# todo:Cleaning
df.drop(['fare', 'home.dest', 'name'], axis=1, inplace=True)
df['age'] = df['age'].fillna(0)

df.hist(bins=20, figsize=(20,15))
plt.show()

# to save original dataset
df_copy = df.copy()

df_copy['age'].iloc[0:10] = 500

# print(df_copy.head(n=15))

df_copy.hist(bins=20, figsize=(20,15))
# plt.show()

# remove all rows that age is greater that 100
df_copy.drop( df_copy[ df_copy['age'] > 100 ]['age'].index, inplace=True)

df_copy.hist(bins=20, figsize=(20,15))
# plt.show()

# (count_of_rows,count_of_column)
print(df_copy.shape)

# I am alive

# count every value of sex column
# print(df['sex'].value_counts())

# todo: survived males
gender_df = df[df['sex'] == 'male']
survived = gender_df[ gender_df['survived']==1 ]

# survived_percentage from male is 19.09%
survived_percentage = ( survived.shape[0] / gender_df.shape[0] ) * 100
# print(survived_percentage)

for gen in df['sex'].unique():
    print(gen)

    gender_df=df[df['sex'] == gen]

    survived=gender_df[gender_df['survived'] == 1]

    survived_percentage=(survived.shape[0] / gender_df.shape[0]) * 100

    print("Count: ",gender_df.shape[0])
    print("Servived  : ","%.2f" % survived_percentage,'%')

    print("\n=====\n")

# unique() to get values in column without repeat
for x_class in df['pclass'].unique():
    print(x_class)

    x_df=df[df['pclass'] == x_class]
    survived=x_df[x_df['survived'] == 1]

    survived_percentage=(survived.shape[0] / x_df.shape[0]) * 100

    print("Count: ",x_df.shape[0])
    print("Servived  : ","%.2f" % survived_percentage,'%')

    print("\n====\n")

df.to_csv('new_set.csv', sep='\t', encoding='utf8' )

new_df = pd.read_csv('new_set.csv', sep='\t' ,encoding='utf8')
print(new_df.head())