import pandas as pd

sem_1=pd.Series(data=[45,25],index=['math','Physics'])
sem_2=pd.Series(data=[64,35,10],index=['Algebra','CS','Physics'])

print(sem_1+sem_2)

# sum intersect only