import pandas as pd

data = {
    'Name': ['nithin', 'nithya', 'nikhil', 'nishanth', 'nihal'],
    'Age' : [24,24,21,20,23],
    'Salary' : [1000,10001,100002,100003,10002],
    'Subject': ['be', 'msc', 'bca', 'mtech', 'bsc'],
    'Marks': [85.5, 80.5, 95.5, 75.5, 65.5]
}

df = pd.DataFrame(data)
df['Grade'] = ['B','B','A','C','D']
first_class_result = df[df['Grade'] == 'A']
print(first_class_result)
print(df)
grouped = df.groupby('Age')['Salary'].mean()
grouped1 = df.groupby('Age')
print(grouped)
print(grouped1.groups)
print(grouped1.get_group(24))
