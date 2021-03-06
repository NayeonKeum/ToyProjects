import pandas as pd
friend_list=[
    ['john', 22, 'student'],
    ['jenny', 27, 'student'],
    ['Jacob', 30, 'developer']
]
column_name=['name', 'age', 'job']
df=pd.DataFrame.from_records(friend_list, columns = column_name)

# 부분 출력
#print(df[1:3])
# or
# 직접 자르기
#df=df[1:3]

# or
# location기능 사용 가능
#print(df.loc[[0, 2]])

# by column condition
    # integer 사용
print(df[df.age>25])
print(df.query('age>25'))
    # + 문자형
print(df[(df.age>25)&(df.name=='Jacob')])

#filter column
    # by index
friend_list=[
    ['John', 22, 'student'],
    ['Jenny', 27, 'teacher'],
    ['Jacob', 30, 'developer']
]
df=pd.DataFrame.from_records(friend_list)
print(df.iloc[:,0:2])
print(df.iloc[0:2,0:2])

    #by column name
df=pd.read_csv('data/friend_list_no_head.csv', header=None, names=['name', 'age', 'job'])
df_filtered=df[['name', 'age']]
#or
print(df.filter(items=['age', 'job']))

print(df.filter(like='a', axis=1))#axis는 축, 언제나 1..?

print(df.filter(regex='b$', axis=1))#regex는 정규식


