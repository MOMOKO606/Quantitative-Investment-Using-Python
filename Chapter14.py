# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:05:50 2017

@author: bianl
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats


#  Exercise 14.1
#  读入excel文件 as DataFrame类型数据
Bwages=pd.read_csv('Bwages.csv')

#  对数据的‘wage’列做直方图
plt.figure()
Bwages.wage.hist(normed=True)  # normed参数表示：是否无量纲化
#  对数据的‘wage’列做累积直方图
plt.figure()
Bwages.wage.hist(normed=True,cumulative=True)

#  求概率密度
kde = stats.gaussian_kde(Bwages.wage)
#  设置plot的x参数
bins=np.linspace(0,100,num=1000)
#  绘制累积分布曲线
plt.figure()
plt.plot(bins,kde(bins).cumsum())


#  Exercise 14.2
history=pd.read_csv('history.csv',index_col='Date')
#  新兴市场基金盈利的月份
history.index[history['Emerging.Markets']>0]
#  新兴市场基金亏损的月份
history.index[history['Emerging.Markets']<=0]
#  盈利率
rate=float(len(history.index[history['Emerging.Markets']>0]))/len(history.index)

print(1-stats.binom.cdf(6,12,rate))


#  Exercise 14.3
from math import sqrt
norm_bins=np.linspace(-5, 5, num=200)

plt.plot(norm_bins,stats.norm.pdf(norm_bins,0,1),label='N(0,1)')

plt.plot(norm_bins,stats.norm.pdf(norm_bins,0,sqrt(0.5)),
         label='N(0,0.5)')

plt.plot(norm_bins,stats.norm.pdf(norm_bins,0,sqrt(2)),label='N(0,2)')

plt.plot(norm_bins,stats.norm.pdf(norm_bins,2,1),label='N(2,1)')

plt.legend()

