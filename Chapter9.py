# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:14:21 2017

@author: bianl
"""

#  Exercise 9.1
import time
import datetime

now=datetime.datetime.now()
print(now.strftime('%y-%m-%d'))

print(time.ctime(time.time()))


#  Exercise 9.2
def CreateUsername():
    name=raw_input('请输入用户名:')
    if not name[0].isalpha():
        print('用户名必须以字母开头')
        return(CreateUsername())
    else:
        return(name)
            
    
def VerifyPassword(psw):
    if psw[0].isalpha() == False:
        print('密码必须以字母开头')
        return(False)
    if psw.find('_') + psw.find('*') + psw.find('#') == -3:
        print('密码需至少包含“_”，“*”，“#”中任意一个')
        return(False)
    if len(psw) < 6:
        print('密码长度必须大于6位')
        return(False)
    return(True)
    
    
def CreatePassword():
    psw=raw_input('请输入密码:')
    is_legal=VerifyPassword(psw)
    if not is_legal:
        return(CreatePassword())
    else:
        return(psw)
            
        
def CreateUser():
    CreateUsername()
    CreatePassword()
    print('用户创建成功！')


''' CreateUser()
'''


#  Exercise 9.3
even1=range(0,101,2)


#  Exercise 9.4
dates=[datetime.datetime(2015,1,13)+datetime.timedelta(i) for i in range(5)]
closes=[7.31,7.28,7.40,7.43,7.41]
prices={dates[i]:closes[i] for i in range(5)}

#  插入prices，注意同时也要插入dates才不会影响后面的迭代调用
prices[datetime.datetime(2015,1,20)]=7.44
dates.append(datetime.datetime(2015,1,20))

prices[datetime.datetime(2015,1,21)-datetime.timedelta(4)]

prices[datetime.datetime(2015,1,16)]=7.50


#  Exercise 9.5
import math
cash=10000

#  传说中的简版“追涨”策略
share={dates[0]:0}
for i in range(1,6):
    if prices[dates[i]] > prices[dates[i-1]]:
        buyshare=math.floor(0.5*cash/prices[dates[i]])
        share[dates[i]]=buyshare
        cash=cash-buyshare*prices[dates[i]]+share[dates[i-1]]*prices[dates[i]]
    else:
        share[dates[i]]=0
        

        
            








