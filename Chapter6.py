# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 13:42:32 2017

@author: bianl
"""

import random


def Exercise61(x):
    if type(x) != int:
        print('ERROR:Please input an integer.')
        return    
    return (x if x%2 == 1 else 0)  


#  Exercise 6.1
print('Please enter a number:')

ans=Exercise61(input())

print(ans)

 
#  Exercise 6.2
a=[random.randint(-50,50) for i in xrange(5)]
 
for i in a:
    str='Big' if i>=0 else 'Small'
    print(str)
     
     
#  Exercise 6.3
a=[]
for i in xrange(5):
     tmp=[random.random() if j != i else 1 for j in xrange(5)]
     a.append(tmp)


#  Exercise 6.4
for i in (-1,0,1,2,39):
    print(i in range(1,4))


#  Exercise 6.5
a=[]
for i in xrange(4):
    tmp=[1.0/(i+j+1) for j in xrange(4)]
    a.append(tmp)