import pandas as pd

friends = [{'age':25, 'job':'student'},
           {'age':30, 'job':'teacher'},
           {'age':25, 'job':'developer'}
]
df=pd.DataFrame(friends, index=['John', 'Jenny', 'Nate'], columns=['age', 'job'])
print(df.drop(['John', 'Nate']))
#삭제를 df에 반영시키려면
# df=df.drop~~이케  or
# df.drop(['John', 'Nate'], inplace=True)


friends = [{'name':'John', 'age':25, 'job':'student'},
           {'name':'Ben', 'age':30, 'job':'teacher'},
           {'name':'Jenny', 'age':25, 'job':'developer'}
]
df=pd.DataFrame(friends, columns=['name', 'age', 'job'])
#index로 삭제해보자
df=df.drop(df.index[[0,2]])

#column value에 따라
df=pd.DataFrame(friends, columns=['name', 'age', 'job'])
df=df[df.age>25]
print(df)

#column 없애기1
df=pd.DataFrame(friends, columns=['name', 'age', 'job'])
df=df.drop('age', axis=1)#axis는 컬럼 중에서 라는 뜻

#column 없애기2
df=pd.DataFrame(friends, columns=['name', 'age', 'job'])
df=df.drop('age', axis=1, inplace=False)
print(df)


