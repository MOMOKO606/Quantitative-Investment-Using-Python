# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 13:14:53 2017

@author: bianl
"""

3==4 in [ 1 ,'345' ,3+4j , 4 in [1 ,2 , 3 ]]

import random
a=[random.normalvariate(0,1) for i in range(20)]

a.sort()

print (a[0],a[-1],sum(a))