# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 00:21:58 2017

@author: bianl
"""

class Account(object):
    '''
    Account class with attributes "name" and "balance"
    '''

    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance


    def draw(self,money):
        if money > self.__balance:
            print('余额不足')
            return
        else:
            self.__balance-=money


    def deposit(self,money):
        self.__balance+=money


    def get_balance(self):
        return(self.__balance)


    def transfer(self,money,target):
        if money > self.__balance:
            print('余额不足')
            return
        else:
            self.draw(money)
            target.deposit(money)


#  Exercise 8.1
a=Account('Sam',1000)

a.deposit(500)
a.draw(1200)

print(a.get_balance())

#  Exercise 8.2
b=Account('John',3000)

a.transfer(200,b)

print(a.get_balance(),b.get_balance())


#  Exercise 8.3
class Credit(Account):

    def __init__(self, name,balance,creditlimit,overdraw):
        self.name=name
        self.__balance=balance
        self.creditlimit=creditlimit
        self.overdraw=overdraw

    def draw(self,money):
        #  取钱金额超过存款+信用
        if self.overdraw + money > self.__balance+self.creditlimit:
            print('余额不足')
            return
        #  取款金额小于存款
        elif money <= self.__balance:
            self.__balance-=money
        #  取款金额大于存款，且小于存款+信用
        else:
            #  还有存款时
            if self.__balance > 0:
                self.overdraw=money-self.__balance
                self.__balance=0            
            #  无存款时
            else:
                self.overdraw+=money

    def get_balance(self):
        return(self.__balance)

c=Credit('Sam',1000,1000,0)
c.draw(700)
print(c.get_balance())
c.draw(1500)
