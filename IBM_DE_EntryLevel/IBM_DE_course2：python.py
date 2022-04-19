print(25//5)

def test(*name):
	print(type(name))

test([1,2,3])

print(dir([1,2,3]))

with open("/Users/yuxichen/Desktop/text", 'r') as text:
	lines = text.readlines()
print(lines[:])

with open("/Users/yuxichen/Desktop/text", 'a') as text:
	text.write('E\n')
print(lines[:])

import pandas as pd
dic = {1:'A', 2:'B', 3:'A'}
df = pd.DataFrame(dic.items())
print(df, '\n')
print(df[1], '\n') # print the column
print(df[1].unique(), '\n')  # 
print(df[df[0]>1], '\n') # only leave the row where column[0] > 1
df1 = df[df[0]>1] # create a new dataframe 
df1.to_csv('/Users/yuxichen/Desktop/df1.csv') # create a csv file 
print(df1.iloc[0,0])
print(df1.loc[1,0])

import numpy as np
a = np.array([1,2,3])
b = np.array([1,2,3])
size = a.size
ndim = a.ndim
shape = a.shape
dtype = a.dtype
print(a[1:3]) #[1,2]
print([1] + [2])
print(a+b)
print(a*b)
print(np.dot(a,b))
print(a+1)
print(a.mean())
print(a.max())
c = np.array([0,np.pi])
print(np.sin(c))
print(np.linspace(-2,2,num=3))