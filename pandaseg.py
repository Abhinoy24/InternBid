import pandas as pd 
import numpy as np 
'''
lst = ['Bid','Ocean','Gangtok']
df = pd.DataFrame(lst)
print(df)
'''
'''
data = {'Name':['Tom','Nick','Jerry','Aish'],
        'Age':[17,18,19,20],
        'Address':['DElhi','KAnpur','Mumbai','gANGTOK'],
        'Qualification':['BTech','MBA','BBA','BCA']}

df = pd.DataFrame(data)
print(df)
columns = list(df)
for i in columns:
    print("\n",df[i][2])
'''

'''
#print(df[['Name','Age']])
for i,j in df.iterrows():
    print(i,' ',j)
    print()
'''

'''
#row2 = data.iloc[3
data = pd.read_csv('nba.csv',index_col="Name")
print(data.head)

'''
'''
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]

print(first,"\n\n\n",second)

row2 = data.iloc[4]

print(row2)
first = data["Age"]
print(first)
'''

'''
dict = {'First Score':[100,90,np.nan,95],
        'Second Score':[30,45,56,np.nan],
        'Third Score':[np.nan,np.nan,np.nan,98.0]}

df = pd.DataFrame(dict)
print(df.isnull())
print(df.notnull())
'''

'''
df = pd.DataFrame()
print(df)
'''
'''
data = {'Name':['Abhik','AIsh','Paras'],
        'Age':[21,22,24],
        'Height':[5.1,5.2,5.5]}
df = pd.DataFrame(data)
print(df)
address = ['GAngtok','RAngpo','MAjitar']
df['Address'] = address
print(df)
cgpa = [9.5,10,8.5]
df['CGPA'] = cgpa
print(df)
'''

'''
data = pd.read_csv('nba.csv',index_col=None)
print(data.head(5))
#data.drop(["Team","Number","Position"],axis = 1,inplace =True)
#print(data.head(10))
new_row = pd.DataFrame({'Name':'KIWI','Team':'BTSV','Number':'17',
                        'Position':'PG','Age':20.0,'Height':5-5,
                        'Weight':130,'College':'SMIT','Salary':700000.0},index = [0])
data = pd.concat([new_row,data]).reset_index(drop = True)
print(data.head(5))

'''

'''
data = pd.read_csv('nba.csv',index_col=None)
first = data[["Name","Age","Height","Weight"]]
print(first)
row2 = data.iloc[[0,3,5,7]]
print(row2)
row1 = data.iloc[[0,3,5,7],[1,2,3,4]]
print(row1)
row2 = data.iloc[::2,[1,2]]
print(row2)
'''

'''
data = {'Name':['Abhik','AIsh','Paras'],
        'Age':[21,22,24],
        'Height':[5.1,5.2,5.5]}
df = pd.DataFrame(data,index = [True,False,True])
print(df.loc[True])
print()
print(df.iloc[1])
#print(df.ix[True])
'''

'''
#data = pd.read_csv("nba1.1.csv")
data = pd.read_csv("nba.csv",index_col="Name")
print(data)
#df = pd.DataFrame(data, index = [0,1,2,3,4,5,6,7,8,9,10,11,12])
#print(df[[True,False,True,False,True,False,True,False,True,False,True,False,True]])
#print(data['Age'] > 25)
#print(data[:10])
#data.dropna(inplace = True)
#print(data)
#print(data.info())
print(data.isna())
'''

#data = pd.read_csv("employees.csv")

'''
print(data)
df = pd.DataFrame(data)
print(data)
print()
bool_series = pd.notnull(data["Gender"])
print(bool_series.head(10))
print(df.notnull())
print(df.fillna(0))
print()
print(df.fillna(method='pad'))
print(df.fillna(method='bfill'))
data["Gender"].fillna("No Gender", inplace = True)
print(data)
'''

'''
new_data = data.dropna(axis = 0, how = 'any')
print(new_data)

print("Old data frame:", len(data))
print("New data frame:", len(new_data))
print("NUmber of rows with atleast 1 NA:",len(data)-len(new_data))

'''

'''
df = pd.DataFrame(data)
#df["Name"] = df["Name"].str.lower()
#df["Gender"] = df["Gender"].str.upper()
#print(df)
#df["Gender"] = df["Gender"].str.split("a" or "e",n=1,expand = True)
print(df)
df["Age"] = df["Age"].replace(22.0, "Twenty Two")

filter = df["Age"] == "Twenty Two"
df.where(filter).dropna()
print(df)
'''
'''
#regex
s = pd.Series(['a1','b2','c3'])
n = s.str.extract(r'([ab])(\d)')
print(n)

print()

s = pd.Series(['b1','c2','d3'])
n = s.str.extract(r'([cd])(\d)')
print(n)
'''
'''
data = pd.date_range('17/12/1996',periods=100,freq='Y')
print(data)
x = datetime.now()
print(x.month,x.year)
'''

'''

data = {'Name':['Abhik','Kiwi','Paras','Anil'],
        'Age':[21,22,24,25],
        'Height':[5.1,5.2,5.5,5.6]}

data1 = {'Name':['Lucky','Nima','Janam','Kimba'],
        'Age':[21,22,24,26],
        'Salary':[25000,50000,55000,56000]}


df = pd.DataFrame(data,index=[0,1,2,3])
df1 = pd.DataFrame(data1, index = [4,1,2,7])
print(df,"\n\n", df1)


frames = [df,df1]
res = pd.concat(frames,keys=['x','y'])
print("\n",res)
'''

#res1 = pd.concat([df,df1],axis = 1,join="inner")
#print("\n",res1)

#res2 = pd.concat([df,df1],axis = 1,join="inner",sort=False)
#print(res2)

#res = df.append(df1)
#print(res)

'''
series = pd.Series()
print(series)

series = pd.Series([1,2,3,4,5])
print(series)
'''
'''
data = pd.read_csv('nba.csv')
x1 = data.ix[0:20,1:3]
print(x1)
'''
'''
Data = [1,2,3,4,5,6,7]
a = pd.Series(Data)
print(a)
Index = ['a','b','c','d','e','f','g']
a1 = pd.Series(Data, index = Index)
print(a1)
'''

'''
dict = {'a':1,'b':2,'c':3,'d':4,'e':5}
series = pd.Series(dict)
print(series)
'''
'''
d1 = [[1,2,3],[4,5,6]]
d2 = [[9,11,13],[15,17,19]]
data = {'First':d1,'Second':d2}
df = pd.DataFrame(data)
print(df)
'''
data = pd.read_csv(filepath_or_buffer = "pokemon.csv")
print(data['Type']=='Electric')