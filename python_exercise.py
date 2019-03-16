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
def solution6(*numbers):  ##加一个*代表输入的这个参数数量是可变的,多个输进去后变成tuple
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

'''
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''
def solution16(*n):
    ret = []
    for num in n:
        if num % 2 != 0:
            ret.append(str(num))
    return ret
#print(','.join(solution16(1,2,3,4,5,6,7,8,9)))

'''
Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a 
transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''
def solution17():
    stop = False
    result = 0
    while not stop:
        item = input()
        if item != '':
            opr = item.split(' ')[0]
            num = int(item.split(' ')[1])
            if opr == 'D':
                result += num
            if opr == 'W':
                result -= num
        else:
            stop = True
    return result
#print(solution17())
    
'''
Question 18
Level 3

Question:
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check 
them according to the above criteria. Passwords that match the criteria are to be printed, 
each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
import re
phone = '123a#s@-456-7890'
infos = re.findall('',phone)   ## findall返回的是一个列表
#print(infos == [])
def solution18(*str1):
    ret = []
    for pw in str1:
        if len(pw) < 6 or len(pw) > 12:
            continue
        else:
            if re.findall('[#$@]',pw) != [] and re.findall('[a-z]',pw) != [] and re.findall('[0-9]',pw) != []\
                    and re.findall('[A-Z]',pw) != []:
                        ret.append(pw)
                
            
    return ret
#print(','.join(solution18('ABd1234@1','a F1#','2w3E*','2We3345')))
    
'''
Question 19
Level 3

Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order 
where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''
## 这道题重点在于利用sorted或者sort函数可以多个属性进行排序的自带功能
#L = [('12', '12'), ('34', '13'), ('32', '15'), ('12', '24'), ('32', '64'), ('32', '11')]
#L.sort(key=lambda x: (x[0], -int(x[1])))  ##这里的x就是指的要排序的整个东西自己,加个负号是说这个要倒序
#print(L)
def solution19(*tuples):
    list1 = list(tuples)
    list1.sort(key = lambda x: (x[0],int(x[1]),int(x[2])))  ##这个是有优先级的，在最前面的优先级最高这样子，交换顺序
                                                                ##就能交换优先级
    return list1
#print(solution19(('Tom', '19', '80'),('John', '20', '90'),('Jony', '17', '91'),('Json', '21', '85'),\
#                 ('Jony', '17', '93')))
    
'''
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, 
between a given range 0 and n.
'''
##这道题的关键是搞懂generator
## generator（生成器）本身也是可以迭代的，yield就是一个生成器
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

#for i in putNumbers(100):   ## putNumbers是一个generator，用来节省内存的，自带next属性，就可以进行迭代了
#    print(i)

'''
Question 21
Level 3

Question£º
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, 
DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to 
compute the distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''
#import math
def solution21():
    stop = False
    x = 0
    y = 0
    while not stop:
        str1 = input()
        if str1 == '':
            stop = True
        else:
            dirt = str1.split(' ')[0]
            num = int(str1.split(' ')[1])
            if dirt == 'UP':
                x += num
            elif dirt == 'DOWN':
                x -= num
            elif dirt == 'LEFT':
                y -= num
            else:
                y += num
    dist = math.sqrt(abs(x)**2+abs(y)**2)
    ## 下面这一步可以用round替代
    dist_int = int(dist)
    if dist - dist_int >=0.5:
        return dist_int + 1
    else:
        return dist_int
   
#print(solution21())
#print(round(3.92123))
'''
Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''
def solution22(str1):
    ret = {}
    list1 = str1.split(' ')
    for item in list1:
        if item not in ret.keys():
            ret[item] = 1
        else:
            ret[item] = ret[item] + 1
#    print(ret)
#    return ret
    for k,v in ret.items():  ## 针对字典同时获取key和value的方法
        print('{0}:{1}'.format(k,v))   ## print指定内容的打印方法
#    for k,v in ret:
#        print(k)
#a = solution22('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.')
        
'''
Question 23
level 1

Question:
    Write a method which can calculate square value of number
'''

def solution23(x):
    return x*x
#print(solution23(23))

'''
Question 24
Level 1

Question:
    Python has many built-in functions, and if you do not know how to use it, 
    you can read document online or find some books. But Python has a built-in document 
    function for every built-in functions.
    Please write a program to print some Python built-in functions documents, 
    such as abs(), int(), raw_input()
And add document for your own function
'''
def solution24(x):
    print(x.__doc__)

#solution24(abs)

'''
Question 25
Level 1

Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
You can init a object with construct parameter or set the value later
'''
#class Person():
#    # Define the class parameter "name"
#    name = "Person"
#    
#    def __init__(self, name = None):
#        # self.name is the instance parameter
#        self.name = name
#
#jeffrey = Person("Jeffrey")
#print("%s name is %s" % (Person.name, jeffrey.name))
#
#nico = Person()
#nico.name = "Nico"
#print("%s name is %s" % (Person.name, nico.name))

'''
Question26:
Define a function which can print a dictionary where the keys are numbers 
between 1 and 3 (both included) and the values are square of keys.
'''
def solution26():
    ret = {}
    for i in range(1,4):
        ret[i] = i**2
    for k,v in ret.items():
        print('{}:{}'.format(k,v))
#solution26()

'''
Question27:
Define a function which can generate and print a list where the values are square of 
numbers between 1 and 20 (both included).
'''
def solution27(x,y):
    return [i*i for i in range(x,y+1)]
#print(solution27(1,20))
    
'''
Question28:
Write a program which can map() to make a list whose elements are 
square of elements in [1,2,3,4,5,6,7,8,9,10].
'''
#li = [1,2,3,4,5,6,7,8,9,10]
#squaredNumbers = map(lambda x: x**2, li)  ## Python3的map返回的是迭代器
#for i in squaredNumbers:
#    print(i)

'''
Question29:
Write a program which can map() and filter() to make a list whose elements are square of 
even number in [1,2,3,4,5,6,7,8,9,10].
'''
def solution29(list1):
    res = []
    ret = map(lambda x: x**2,filter(lambda x: x%2==0, list1))
    for i in ret:
        res.append(i)
    return res
#print(solution29([1,2,3,4,5,6,7,8,9,10]))
