# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:59:24 2017

@author: bianl
"""

#  Exercise 7.2
def sum_list(x,y):
    if len(x) != len(y):
        print('Error')
        return        
    return([x[i]+y[i] for i in xrange(len(x))]) 
      
a=[2,6,4,8,12]
b=[56,76,1,2,3]

print(sum_list(a,b))
                  

#  Exercise 7.3
def sum2(*lists):
    if len(lists) == 2:
        return (sum_list(lists[0],lists[1]))
    else:
        return (sum_list(lists[0],sum2(*lists[1:])))  
      
c=[1,2,3,4,5]
d=[2,5,7,2,1]
e=[0,2,3,4,5]

print(sum2(a,b,c,d,e))


#  Exercise 7.4
def Fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_recursive(n-1)+Fibonacci_recursive(n-2)
    
def Fibonacci_iterative(n):
    F=[0,1]
    if n < 2:
        return F[n]
    else:
        for i in xrange(2,n+1):
            tmp=F[i-1]+F[i-2]
            F.append(tmp)     
        return F[-1]

print(Fibonacci_iterative(7))


#  Exercise 7.5
g=[-2,-4,-9]
print(map(abs,g))


#  Exercise 7.6
def NonNagNum(y):
    return (sum(map(lambda x:x>0,y)))

share=[-0.3,0.2,3,-3,-2]
print(NonNagNum(share))



