# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:25:58 2019

@author: pengz
"""

#######求100以内的素数#########
#for i in range(2,100):
#    isPrime = True
#    for j in range(2,i): 
#        remainder = i%j
#        if remainder == 0:
#            isPrime = False 
#    if isPrime:
#        print(i)

######判断一个数是不是prime######
def number_isPrime(x):   ##Written by myself
    prime = True
    for i in range(2,x): ##其实可以不到x-1,到根号x+2就行了,节省时间复杂度
        remainder = x%i  
        if remainder == 0:
            prime = False
            break
    return prime
#print(numberisPrime(13195))
#
########用递归求100以内的#############
########关键在于用递归的方法来判断一个数是不是prime########
#import math
def numberisPrime(x,a):
    if a == 1:
        return True
    if x%a == 0:
        return False
    else:
        return numberisPrime(x,a-1)

def prime_below(n):
    primes_list = []
    for i in range(2,n+1):
        if numberisPrime(i,i//2):   ##这里相当于用i//2来代替上面的x-1
            primes_list.append(i)
    return primes_list

#print(prime_below(100))       
#
#
###########找一个数的最大质因数#############################
def findPrime(x,factor): #只能用于数字比较小的时候
    if x == 1:
        return factor
#    elif numberisPrime(int(x)):
#        print("is prime")
    else:
        
        if x % factor ==0:
    #        result = factor
            x = x/factor
            
            return findPrime(x,factor)
        else:
            factor += 1
            return findPrime(x,factor)
#    
#print(findPrime(13195,2))
#
def findPrimelarge(x,factor): #算数字比较大的时候
    if numberisPrime(x):
        return x
    else:
#        result = 1
        while x > 1:   ##也就是直到x==1时，跳出循环
            if x % factor == 0:
                result = factor
                x = x/factor
                while x % factor == 0:
                    x = x/factor
            factor += 1
        return result
#
#print(findPrimelarge(600851475143,2))