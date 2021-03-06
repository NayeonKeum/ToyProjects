import pandas as pd
df=pd.read_csv('data/friend_list.csv')

df1=pd.read_csv('data/friend_list.txt')

df2=pd.read_csv('data/friend_list_tab.txt', delimiter='\t')

df3=pd.read_csv('data/friend_list_no_head.csv', header=None)
df3.columns=['name', 'age', 'job']

df4=pd.read_csv('data/friend_list_no_head.csv', header=None, names=['name', 'age', 'job'])
print(df4)
