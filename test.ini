import os
import sys
import pandas as pd
import gugu as gg

obj = gg.StockData('002231') 
obj.history(start='2017-10-02', end='2020-11-17')
df = obj._data
print(df)
#print(df[(df.close-df.open)/df.open > 0.096])
df2 = df.copy()
df2['rate'] = 0

#get rate
df2['rate'] = (df2['close'].shift(0) - df2['close'].shift(1))/df2['close'].shift(1)
#df3= df2[df2['rate']>0.096]

#当日的最大值率，有最大值除以开始的值
df2['highrate'] = (df2['high']-df2['open'])/df2['open']
df2['lowrate'] = (df2['low']-df2['open'])/df2['open']


#get the object row
mask = (df2['rate'].shift(0)>0.096)|(df2['rate'].shift(1)>0.096)|(df2['rate'].shift(2)>0.096)|(df2['rate'].shift(3)>0.096)|(df2['rate'].shift(4)>0.096)
df3 = df2[mask]
print(df3)

print(df3.to_numpy())

df3.to_csv('foo1.csv')

#df2[mask].to_csv('foo1.csv')
np3 = df3.to_numpy();
np4 = np3.reshape((50,));

print(np4)

print ("hello world")
df4 = df[['open','close']]
df5 = df.loc[:,'open':'close']
#print(df3)
print(df4)
print(df)


