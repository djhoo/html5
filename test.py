import os
import sys
import pandas as pd
import gugu as gg
import numpy as np

obj = gg.StockData('002231') 
obj.history(start='2017-01-01', end='2019-12-30')
df = obj._data
print(df)
#print(df[(df.close-df.open)/df.open > 0.096])
df2 = df.copy()
df2['rate'] = 0

#get rate
df2['rate'] = (df2['close'].shift(0) - df2['close'].shift(1))/df2['close'].shift(1)
#df3= df2[df2['rate']>0.096]

#当日的最大值率，用最大值除以开始的值
df2['highrate'] = (df2['high']-df2['open'])/df2['open']
df2['lowrate'] = (df2['low']-df2['open'])/df2['open']


#get the object row
#mask = (df2['rate'].shift(0)>0.096)|\
#        ((df2['rate'].shift(1)>0.096)&(df2['rate'].shift(0)<=0.096))|\
#            ((df2['rate'].shift(2)>0.096)&(df2['rate'].shift(0)<=0.096))|\
#                ((df2['rate'].shift(3)>0.096)&(df2['rate'].shift(0)<=0.096))|\
#                    ((df2['rate'].shift(4)>0.096)&(df2['rate'].shift(0)<=0.096))
#mask = (df2['rate'].shift(0)<-0.096)|(df2['rate'].shift(1)<-0.096)|(df2['rate'].shift(2)<-0.096)|(df2['rate'].shift(3)<-0.096)|(df2['rate'].shift(4)<-0.096)
#mask = ((df2['rate'].shift(0)>0.096)|(df2['rate'].shift(1)>0.096)|(df2['rate'].shift(2)>0.096)|(df2['rate'].shift(3)>0.096)|(df2['rate'].shift(4)>0.096))&(df2['rate'].shift(-1)<=0.096)
mask = ((df2['rate'].shift(0)>0.096)&(df2['rate'].shift(-1)<=0.096)&(df2['rate'].shift(-2)<=0.096)&(df2['rate'].shift(-3)<=0.096)&(df2['rate'].shift(-4)<=0.096))|\
    ((df2['rate'].shift(0)<=0.096)&(df2['rate'].shift(1)>0.096)&(df2['rate'].shift(-1)<=0.096)&(df2['rate'].shift(-2)<=0.096)&(df2['rate'].shift(-3)<=0.096))|\
        ((df2['rate'].shift(0)<=0.096)&(df2['rate'].shift(1)<=0.096)&(df2['rate'].shift(2)>0.096)&(df2['rate'].shift(-1)<=0.096)&(df2['rate'].shift(-2)<=0.096))|\
            ((df2['rate'].shift(0)<=0.096)&(df2['rate'].shift(1)<=0.096)&(df2['rate'].shift(2)<=0.096)&(df2['rate'].shift(3)>0.096)&(df2['rate'].shift(-1)<=0.096))|\
                ((df2['rate'].shift(0)<=0.096)&(df2['rate'].shift(1)<=0.096)&(df2['rate'].shift(2)<=0.096)&(df2['rate'].shift(3)<=0.096)&(df2['rate'].shift(4)>0.096))

df3 = df2[mask]

df4 = df3[['date','volume','highrate','lowrate','rate']]
print(df4)

rowsize = df4.shape[0]
leftsize = rowsize % 5
df4.drop(df4.tail(leftsize).index)

print(df4)
#df4.to_csv('foo1.csv')

np4 = df4.to_numpy();
np5 = np4.reshape((-1,25));
#df5 = df4.values.reshape((25,-1))
#numpy.savetxt("foo.csv", a, delimiter=",")
#pd.DataFrame(np5).to_csv("foo1.csv")
pd5 = pd.DataFrame(np5)
print(pd5)
pd6 = pd5.drop(pd5.columns[[5,10,15,20]], axis=1)
pd6.columns = ['date','volume1','highrate1','lowrate1','rate1','volume2','highrate2','lowrate2','rate2','volume3','highrate3','lowrate3',\
    'rate3','volume4','highrate4','lowrate4','rate4','volume5','highrate5','lowrate5','rate5']

pd6['volume1'] = pd6['volume1'] / pd6['volume2']
pd6['volume3'] = pd6['volume3'] / pd6['volume2']
pd6['volume4'] = pd6['volume4'] / pd6['volume2']
pd6['volume5'] = pd6['volume5'] / pd6['volume2']
pd6['volume2'] = 1

print(pd6)


pd6.to_csv('foo1.csv')

print ("hello world")
#print(df3)
