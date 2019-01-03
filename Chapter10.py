# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 14:42:11 2017

@author: bianl
"""

#  Exercise 10.1
import numpy as np
hilbert=np.array([[1.0/(i+j+1) for j in range(1,5)] for i in range(1,5)])


#  Exercise 10.2
import datetime as dt
import math

#  构建日期-收盘价的dict
dates=[dt.datetime(2015,1,13)+dt.timedelta(i) for i in range(5)]
closes=[7.31,7.28,7.40,7.43,7.41]

prices={dates[i]:closes[i] for i in range(5)}

dates.append(dt.datetime(2015,1,20))
prices[dt.datetime(2015,1,20)]=7.44
#  初始资产10000元
cash=10000
#  通过“追高策略“创建股票份额dict
share={dt.datetime(2015,1,13):0}

for i in range(1,6):
    if prices[dates[i]] > prices[dates[i-1]]:
        buyshare=math.floor(0.5*cash/prices[dates[i]])
        share[dates[i]]=buyshare
        cash=cash-buyshare*prices[dates[i]]+share[dates[i-1]]*prices[dates[i]]
    else:
        share[dates[i]]=0

#  查找购买日期(通过numpy.datetime64)      
buydate1=[np.datetime64(date) for date in share.keys() if share[date]>0]
#  查找购买日期
buydate2=[date for date in share.keys() if share[date]>0]       
    

#  Exercise 10.3
step=2*np.pi/1000
y=[np.cos(x) for x in np.arange(0,2*np.pi+step,step)]

cosin=np.cos(np.linspace(0,2*np.pi,1001))


#  Exercise 10.4
sample=np.array([0.5,1.43,-1.36,-0.16,0.29,-0.59,1.16,-0.33,0.07,-1.36])
print(np.mean(sample),np.var(sample),np.std(sample),np.median)