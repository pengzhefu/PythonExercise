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
            
"""对于给定的n, 使factor = 2, 3, 4, 5, 6...,
对于每个factor, 当factor能被n完全整除时, 就到下一个factor.
可以预见, 所有被整除的factor都是质因数,
当所有小的因数都被整除时, n将会变为1
如n为20, factor为2时, 20 % 2 = 0, n = n / 2, n变为10,
return factor为10,
10 % 2 = 0, n = n / 2, n变为5, (整除时将某一个因数整除完)
然后下一个factor3, 4, 5, n % 5 = 0,
return factor = 5, n变为1, 跳出循环
"""
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
'''
#----------------------------------------#
Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
def solution1(x,y):
    ret = []
    for number in range(x,y+1):
        if ((number%7) == 0) and ((number % 5)!= 0):
            ret.append(str(number))
    return ret
#a = solution1(2000,3200)
#print(','.join(a))  ##join方法必须保持前后的变量的一致性，前面要了str类型的，就要后面也是str

'''
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''
def solution2(x):
    if x == 1:
        return x
    else:
        return x*solution2(x-1)
#print(solution2(8))

'''
Question 3
Level 1

Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
such that is an integral number between 1 and n (both included). and then the program 
should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

'''
def solution3(n):
    ret = []
    for i in range(1,n+1):
        ret.append((i,i*i))
    dic = dict(ret)
    return dic
#print(solution3(17))

'''
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a 
tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''
#str1 = input("Please input your number:")
def solution4():
    str1 = input("Please input your number:")
    list1 = str1.split(',')
    print(list1)
    print(tuple(list1))
#solution4()

'''
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
class Question5():
    def __init__(self,string = None):
#        pass
        self.string = string
    def getString(self):
        self.string = input("Please enter the string: ")
    def printString(self):
        print(self.string.upper())

#q5 = Question5()
#q5.getString()
#q5.printString()

'''
Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''
import math
def solution6(*numbers):  ##加一个*代表输入的这个参数数量是可变的
    list2 = []
#    input1 = input("Please enter the number you want to cal: ")
#    list1 = input1.split(',')
    for item in numbers:
        Q = math.sqrt((2*50*item)/30)
        list2.append(str(Q))
    print(",".join(list2))
#solution6(100,150,180)

'''
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The 
element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
'''
def solution7(x,y):
    ret = [[] for i in range(x)] ##快速创造多个相同的list的办法
    j = 0
    for each_list in ret:
        for k in range(y):
            each_list.append(k*j)
        j+= 1
    return ret
#print(solution7(3,5)) 

'''
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints 
the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''
def solution8():
    str1 = input("Please enter your words: ")
    list1 = str1.split(',')
    list1.sort()
    print(','.join(list1))
#solution8()
    
'''
Question 9
Level 2

Question
Write a program that accepts sequence of lines as input and prints the lines after 
making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''
def solution9_1():
    end = False
    ret = []
    while not end:
        str1 = input("Please enter your sentence: ")
        if str1 == '':
            end = True
        else:
            ret.append(str1)
    for sentence in ret:
        print(sentence.upper())

#solution9_1()

def solution9_2(*str1):
    ret = []
    for sentence in str1:
        ret.append(sentence.upper())
    return ret
#print('\n'.join(solution9_2('abc','yui')))

'''
Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words 
as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''
def solution10_1():
    str1 = input("Please enter your words: ")
    list1 = str1.split(' ')
#    list1.sort()
    list2 = list1.reverse()
    set1 = set(list1)
    list2 = list(set1)
    list2.sort()
    return list2
#print(' '.join(solution10_1()))

def solution10_2(str1):
    list1 = str1.split(' ')
    set1 = set(list1)
    list2 = list(set1)
    list2.sort()
    return list2
#print(' '.join(solution10_2('hello world and practice makes perfect and hello world again')))

'''
Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 
4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers 
that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''
def b2t(str1):  ##二进制转换成十进制
    result = 0
    i = len(str1) - 1
    j=0
    while i >= 0:
        result += int(str1[i])*(2**j)
        j += 1
        i -= 1
    return result
## Python自带转换进制的函数，intp，用法为：intp(str1,x进制) 如：intp('0110',2)
def solution11():
    str1 = input("Please enter the number you want: ")
    list1 = str1.split(',')
    list2 = []
    ret = []
    for item in list1:
        num = b2t(item)
        list2.append(num)
    for i in range(len(list2)):
        if list2[i] % 5 == 0:
            ret.append(list1[i])
    print(','.join(ret))
#solution11()

'''
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 
3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
def solution12(x,y):
    ret = []
    for i in range(x,y+1):
        str1 = str(i)
        even = True
        for single in str1:
            if int(single) % 2 != 0:
                even = False
        if even:
            ret.append(str(i)) 
    return ret
#print(','.join(solution12(2000,3001)))

'''
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
def solution13(str1):
    num_l = 0
    num_d = 0
    for item in str1:
        if item.isalpha():  ## isalpha()是判断一个字符串是否全为字母
            num_l += 1      
        if item.isdigit():  ## isdigit()是判断一个字符串是否全为数字
            num_d += 1
    print("LETTERS",num_l)
    print("DIGITS", num_d)
#solution13('hello world! 123')
    
'''
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper 
case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
def solution14(str1):
    num_u = 0
    num_l = 0
    for item in str1:
        if item.isupper():  ## isalpha()是判断一个字符串是否全为字母
            num_u += 1      
        if item.islower():  ## isdigit()是判断一个字符串是否全为数字
            num_l += 1
    print("UPPER CASE",num_u)
    print("LOWER CASE", num_l)
#solution14('Hello world!')

'''
Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''
def solution15(x):
    return (x+11*x+111*x+1111*x)
#print(solution15(9))
