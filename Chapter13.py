# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 12:42:10 2017

@author: bianl
"""

import pandas as pd
import matplotlib.pyplot as plt

#  读入excel文件并指定index列
history=pd.read_csv('history.csv',index_col = 'Date')
#  通过to_datetime将index列转换成datetime对象
history.index = pd.to_datetime(history.index,format='%Y-%m-%d')

#  Exercise 13.1
history.head()
history['Emerging.Markets'].mean()
history['Emerging.Markets'].median()
history['Emerging.Markets'].mode()
history['Emerging.Markets'].quantile([0.1,0.9])


#  Exercise 13.2
history['Event.Driven'].max()-history['Event.Driven'].min()
history['Event.Driven'].mad()
history['Event.Driven'].var()
history['Event.Driven'].std()


#  Exercise 13.3
history[['Relative.Value','Fixed.Income.Arbitrage']].plot()
history['Relative.Value'].mean() 
history['Fixed.Income.Arbitrage'].mean() 
history['Relative.Value'].std() 
history['Fixed.Income.Arbitrage'].std() 