# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:07:14 2017

@author: bianl
"""



a=tuple(range(1,11))

b=tuple(i for i in range(1,21) if i%2 == 1)

c=[i for i in xrange(1,51) if i%5 == 0]

d=[]
for i in xrange(1,6):
    for j in xrange(3):
        d.append(i)
        
e={'NASDAQ','Dowjones','DAX','FTSE'}