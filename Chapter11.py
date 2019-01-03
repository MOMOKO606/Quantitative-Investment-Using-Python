# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 17:47:44 2017

@author: bianl
"""

#  Exercise 11.1
import numpy as np
a=np.array([i for i in range(1,20,2)])


#  Exercise 11.2
b=np.array(tuple(i for i in range(40) if i%3 == 0))


#  Exercise 11.3
same=a[np.in1d(a,b)]
print(same[:len(same)/2])


#  Exercise 11.4
print(np.random.uniform(0,10,10))


#  Exercise 11.5
a=np.arange(2,22,2)
print(a[-5:])


#  Exercise 11.6
import pandas as pd
data=pd.DataFrame({'id':['a','b','c','d','e','f'],\
                   'name':['Alice','Bob','Charlie','David','Esther','Fanny'],\
                   'age':[34,36,20,29,32,36]})
data.T.iloc[2]

new=pd.DataFrame({'id':['g'],'name':['John'],'age':[19]})


newdata=data.append(new)

newdata.index=newdata.age