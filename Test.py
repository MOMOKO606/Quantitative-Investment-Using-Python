# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 00:33:27 2017

@author: bianl
"""


#  Exercise 3.4
a=([i for i in range(1,10)])
b=([i for i in range(20) if i%2==1])
c=[i for i in range(1,50) if i%5==0]
d=[i for i in range(1,6) for j in range(3)]
e={'NASDAQ','Dowjones','DAX','FTSE'}


#  Exercise 5.5
import random
l=[random.normalvariate(0,1) for i in range(20)]
l.sort()
print(l[0],l[-1],sum(l))


#  Exercise 6.1
def IsoddInt(x):
    if type(x) != int:
        print('ERROR:Please inpput an integer.')
        return
    return(x if x%2==1 else 0)
    

#  Exercise 6.2
import random
l=[random.randint(-50,50) for i in xrange(5)]
for i in xrange(5):
    str=('Big' if l[i] > 0 else 'Small')
    print(str)
    
    
#  Exercise 6.3
diag=[[0 if i!=j else 1 for i in xrange(5)] for j in xrange(5)]



#  Exercise 6.5
h=[[1.0/(i+j+1) for j in xrange(1,5)] for i in xrange(1,5)]



#  Exercise 7.1
x=[1,2,3]

def permutation(x):
    x[0],x[-1]=x[-1],x[0]
    return(x)
    
y=permutation(x)

print(y is x)


#  Exercise 7.2
def sum_lists(x,y):
    if len(x) != len(y):
        print('Error!')
        return
    n=len(x)
    return([x[i]+y[i] for i in xrange(n)])
    
a=[2,6,4,8,12]
b=[56,76,1,2,3]

print(sum_lists(a,b))


#  Exercise 7.3
def sum2(*l):
    n=len(l)
    if n == 2:
        return(sum_lists(l[0],l[1]))
    return(sum_lists(l[0],sum2(*l[1:])))


c=[1,2,3,4,5]
d=[2,5,7,2,1]
e=[0,2,3,4,5]

print(sum2(a,b,c,d,e))


#  Exercise 7.4
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return(fibo(n-1)+fibo(n-2))

    
#  Exercise 7.6
list=[-0.4,-2,0,1,2,3]
f=lambda x:x>0
print(sum(map(f,list)))


#  Exercise 9.2
def CreateUser():
    CreateName()
    CreatePsw()
    print('用户创建成功')
     

def CreateName():
    name=raw_input('Please input Username:')
    if name[0].isalpha():
        return name
    else:
        print('Username must started with a letter')
        return(CreateName())
        
def CreatePsw():
    psw=raw_input('Please input Password:')
    is_legal=VerifiedPsw(psw)
    if is_legal:
        return psw
    else:
        CreatePsw()
        
def VerifiedPsw(psw):
    if not psw[0].isalpha():
        return False
    if psw.find('_') + psw.find('*') + psw.find('#') == -3:
        print('密码需至少包含“_”，“*”，“#”中任意一个')
        return(False)
    if len(psw) < 6:
        print('密码长度必须大于6位')
        return(False)
    return(True) 
            
CreateUser()


class Account(object):
    def __int__(self,name,balance):
        self.name=name
        self.__balance=balance
        
    def deposit(self,money):
        self.__balance+=money
        
    def withdraw(self,money):
        if self.__balance < money:
            print('余额不足')
            return
        else:
            self.__balance-=money
            
    def get_balance(self):
        return(self.__balance)

    def transfer(self,money,target):
        if money >= self.__balance:
            print('Error!')
            return
        else:
            target.deposit(money)
            self.withdraw(money)



account1=Account()
account1.name='Sam'
account1.balance=1000

account2=Account()
account2.name='John'
account2.balance=3000


#  Exercise 9.4
import datetime as dt

dates=[dt.datetime(2015,1,13)+dt.timedelta(i) for i in xrange(5)]
closes=[7.31,7.28,7.40,7.43,7.41]

prices={dates[i]:closes[i] for i in xrange(5)}

dates.append(dt.datetime(2015,1,20))
prices[dt.datetime(2015,1,20)]=7.44


prices[dt.datetime(2015,1,21)-dt.timedelta(4)]

prices[dt.datetime(2015,1,16)]=7.50
    

#  Exercise 9.5
import math
cash=10000

shares={dates[0]:0}

for i in xrange(1,len(dates)):
    if prices[dates[i]] > prices[dates[i-1]]:
        shares[dates[i]]=math.floor(0.5*cash/prices[dates[i]])
        cash=cash-prices[dates[i]]*shares[dates[i]]+prices[dates[i]]*shares[dates[i-1]]
    else:
        shares[dates[i]]=0
            
        
    
