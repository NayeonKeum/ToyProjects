import pandas as pd
friends=[{'name':'EnJae', 'age':22, 'job':'student'},
         {'name':'Jenny', 'age':30, 'job': None},
         {'name':'Nate', 'age':30, 'job':'teacher'}]
df=pd.DataFrame(friends)
df=df[['name', 'age', 'job']]

#csv로 저장하기(index와 header는 True default-생략 원할 때 False로 주면 됨)
#na_rep는 None value를 위한
df.to_csv('data/friend.csv', index=False, header=True, na_rep='-')
