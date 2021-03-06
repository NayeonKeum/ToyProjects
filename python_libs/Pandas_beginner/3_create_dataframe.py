import pandas as pd

friend_dict_list = [
    {'name':'John', 'age':25, 'job':'student'},
    {'name':'Nate', 'age':30, 'job':'teacher'}
]
df=pd.DataFrame(friend_dict_list)
df=df[['name', 'job', 'age']]


from collections import OrderedDict
friend_ordered_list = OrderedDict(
    [
        ('name', ['John', 'Nate']),
        ('age', [20, 30]),
        ('job', ['student', 'teacher'])
    ]
)
df=pd.DataFrame.from_dict(friend_ordered_list)



friend_list=[
    ['john', 22, 'student'],
    ['jenny', 22, 'student']
]
column_name=['name', 'age', 'job']
df=pd.DataFrame.from_records(friend_list, columns = column_name)


friend_list = [
    ['name', ['John', 'Nate']],
    ['age', [20, 30]],
    ['job', ['student', 'teacher']]
]

df=pd.DataFrame.from_items(friend_list)
print(df)
