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
df4.to_csv('foo1.csv')

np4 = df4.to_numpy();
np5 = np4.reshape((25,));
print(np5)


print(rowsize)
print(leftsize)



#df2[mask].to_csv('foo1.csv')
np3 = df3.to_numpy();
#np4 = np3.reshape((50,));

print ("hello world")
#print(df3)
