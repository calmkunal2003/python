# print(100+2)
#
# print (list(i for i in range(0,10)))

#list2= [i**2 for i in range(0,10) if i%2==0]

#special for loop, how it works :

# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             next(iterator)
#         except StopIteration:
#             break
#
# special_for([1, 2, 3])
#
#
# ##  ****** range function  ***
#
# class MyGen():
#     current = 0
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#        if MyGen.current < self.last:
#            num = MyGen.current
#            MyGen.current +=1
#            return  num
#        raise StopIteration
#
#
# gen = MyGen(0,10)
# for i in gen:
#     print(i)

###  Fibonacci series
 # with geenrator
# def fib(num):
#     a=0
#     b=1
#     for i in range(num):
#         yield a
#         temp = a
#         a = b
#         b = temp + b
# for x in fib(21):
#     print (x)

# with list

# def fib_list(num):
#     a=0
#     b=1
#     result = []
#     for i in range(num):
#         result.append(a)
#         temp = a
#         a = b
#         b = temp + b
#     return result
# print (fib_list(20))
#
# # Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
# #
# l=[]
# for i in range(2000,3200):
#     if (i%7==0 )and (i%5!=0):
#         #l.append(str(i))
#         print(i, end=',')
#
# #print (',',l)

## Factorial of a number
## wHILE loop
# n = int(input("Enter the number to find Factorial:"))
# i = 1
# fact =1
# while i <= n:
#     fact = fact * i
#     i = i+1
# print("factorial of ",n, "is :",fact)

## Using for loop
# n = int(input("Enter the number to find Factorial:"))
# fact =1
# for i in range(1, n+1):
#     fact = fact * i
# print("factorial of ",n, "is :",fact)

#Using Lambda expression:

# n = int(input("Enter the number to find Factorial:"))
#
# def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
# print(shortFact(n))


#With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

#Then, the output should be:

#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# n = int(input())
# x ={i:i*i for i in range(1, n+1) } # using dictionary comprehension
# print(x)


# n = int(input())
# val = {}
# for i in range(1,n+1):
#     val[i]=i*i
# print(val)
#
# n = input()
# l = n.split(",")
# t = tuple(l)

#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.

# class Strings():
#     def __init__(self,string2):
#
#         self.string2=string2
#
#     def getString(self):
#        self.string1 = input("please input a string")
#
#     def printString(self):
#         print(self.string1.upper())
#         print(self.string2.upper())
#
#     def test(self):
#         pass
#
# obj_str = Strings("hello")
#
# obj_str.getString()
# obj_str.printString()

# import math
#
# C,H = 50,30
# #
# # def calcu(D):
# #     return math.sqrt((2*C*D)/H)
# #
# D = input().split(",")
# D = [int(i) for i in D] # converts string to integer
# D = [calcu(i) for i in D] # returns floating value by calc method for every item in D
# D = [round(i) for i in D] # D = [round(i) for i in D] #
# D = [str(i) for i in D] # All the integers are converted to string to be able to apply join operation

# # using list comprehension
# D = [str(round(calcu(int(i)))) for i in D]
# print (",".join(D))

# #### OR using map
#
#
# def calc(D):
#     D= int(D)
#     return str(int(math.sqrt((2*C*D)/H)))
# D = input().split(",")
# D = list(map(calc,D))  # applying calc function on D and storing as a list
# print (",".join(D))

# x,y = map(int,input().split(","))
# # val = input().split(",")
# # x = int(val[0])
# # y = int(val[1])
# # list =[]
# # for i in range(x):
# #     tmp = []
# #     for j in range(y):
# #         tmp.append(i*j)
# #     list.append(tmp)
#
# #### OR Using LIst Comprehension
# lst = [[i*j for j in range(y)] for i in range(x)]
# #lst = [[[i*j*k for k in range(z)] for j in range(y) ] for i in range(x)]
# print (lst)

# items = input().split(",")
# items.sort()
# print(",".join(items))

# Question:
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

# lst=[]
# while True:
#     x = input()
#     if len(x)==0:
#         break
#     lst.append(x.upper())
# for line in lst:
#     print(line)

# word = sorted(list(set(input().split(" "))))  #  input string splits -> converting into set() to store unique
# #  element -> converting into list to be able to apply sort
# print(" ".join(word))

#Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
# number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

# lst = [str(i) for i in range(1000,3001)]
# # # using lambda to define function inside filter function
# lst = list(filter(lambda i:all(ord(j)%2 == 0 for j in i),lst))
# print (",".join(lst))
# import testfile_1
#
# print (testfile_1)
# def multiply(num1,num2):
#     return num1*num2
#
# print(multiply(2,3))

# import random
# my_list=[1,5,4,3]
# random.shuffle(my_list)
# print(my_list)

# import sys
# from random import randint
#
# answer = randint(1,10)
#
# while True:
#     try:
#         guess = int(input("guess the number 1~10: "))
#         if 0 < guess < 11:
#             if guess == answer:
#                 print("you are a genius")
#                 break
#         else:
#             print("i said 1-10")
#     except ValueError:
#         print ("enter a number")
#         continue

##FILEs in python
#
# my_file = open("testfile_1.py")
# print(my_file.readline())
#
# # 'r+' and 'w' mode over writes the file
# #with open("test.txt", mode ='r+') as my_file:
# with open("test.txt", mode='a') as my_file:  # append mode
#     text = my_file.write(" and we are champions")
#     print(text)

## script to translate to diffrent language
# from translate import Translator
#
# translator= Translator(to_lang='es')
#
# try:
#     with open("test.txt", mode = 'r') as my_file:
#         text= my_file.read()
#         translation= translator.translate(text)
#         print(translation)
#         print(my_file.__dir__())
#         with open('./test-espa.txt', mode ='w') as my_new_file:
#             my_new_file.write(translation)
# except FileNotFoundError as e:
#     print("check the file path:")
#
''' **********  REgular Expression ***'''

# import re
# pattern2 = re.compile(r"([a-zA-Z0-9$%#@]{8,})\d") # {8,} - 8 or more character long
# pattern = re.compile(r"([a-zA-z]).([a])") # search letter followed by (.)anything followed by 'a'
# pattern1 = re.compile(r"(^[a-zA-z0-9$-.]+@[a-zA-z0-9]+\.[a-zA-Z0-9.]+$)")
# email = 'cal@gmail.co.in'
# password = 'sear@#$48'
# #a=(re.search('this', string))
# #print(a.end(),a.group(),a.start(),a.span())
#
# # a=pattern.findall(string)
# # b= pattern.match(string) # matches if given from beginning, doesnt matter whats afterwards
# # c= pattern.fullmatch(string) # has to match everything
# e = pattern1.search(email)
# d = pattern2.search(password)
# print(e)
# print (d)

# -- o/p
# <re.Match object; span=(0, 15), match='cal@gmail.co.in'>
# <re.Match object; span=(0, 9), match='sear@#$48'>
#
# from PIL import Image
# img = Image.open("C:\Users\calmk\Downloads\python_projects\example1\download.jpe")
#
''' A website requires the users to input username and password to 
register. Write a program to check the validity of password input by 
users.
 '''
# import re
# string = input().split(",")
# string = str(string)
# #string = "ABd1234@1,a F1#,2w3E*,2We3345"
# print(string)
# pattern = re.compile(r"([a-zA-Z0-9$#@+]{6,12})")
#                    # (r"([a-zA-Z0-9$%#@]{8,})\d")
# check=pattern.search(string)
# print(check.group())

''' You are required to write a program to sort the (name, age, score) tuples 
by ascending order where name is string, age and score are numbers. 
The tuples are input by console. The sort criteria is:name , age, score 
'''
# lst=[]
# while True:
#
#     user_input = input().split(",")
#     if not user_input[0]:
#         break
#     lst.append(tuple(user_input))
# lst.sort(key= lambda x:(x[0],x[1],x[2]))
# print(lst)

''' Define a class with a generator which can iterate the numbers, 
which are divisible by 7, between a given range 0 and n. '''
# class Test:
#     def gen(self,n):
#         return [i for i in range(0,n) if i%7==0]
# n=int(input())
# list=Test().gen(n)
# print(list)

### decorator

from datetime import datetime
#
# def decorator_exp (func):
#     def wrapper_for_func():
#         print("doing this before calling func ****")
#         func()
#         print("doing this after calling func ####")
#     return wrapper_for_func()
# @decorator_exp
# def this_is_func():
#     print("i am that func ")

#this_is_func()

# this_is_func=decorator_exp(this_is_func)
#
# this_is_func( )

#def deorator(func):
#     def wrapper():
#         if 7 <= datetime.now.hour < 22:
#             func()
#         else:
#             pass
#     return wrapper()
# def say_day():
#     print("its the day lets go*****")
#
# say_day()
#
# say_day= deorator(say_day)
#
# say_day()
'''multiple decorator ..the func at top is called first 
then the next and at last the main function
'''
# def mainfun(func):
#     def wrap():
#         print("some")
#         func()
#         print("some ***")
#     return wrap()
#
# def rainfun(func):
#     def wrap():
#         print("rain")
#         func()
#         print("rainy ***")
#     return wrap()
#
# @mainfun
# @rainfun
# def orig():
#     print ("hi")
#
# orig()
'''Define a class with a generator which can iterate the numbers, 
which are divisible by 7, between a given range 0 and n.'''
# input_new = int(input())
# t = [i for i in range(input_new) if i%7==0]
# print(t)

# ##### using class with  Generator function
# class Test:
#     def generator_test(self,n):
#         return [i for i in range(n) if i%7==0]
#
# n = int(input())
# call=Test()
# lst=call.generator_test(n)
# print(lst)

'''Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically.'''

# ss = input().split()
# dict# sets dictionary as i-> split word & ss.count(i) -> total occurrence of i in ss
# dict = {i:ss.count(i) for i in ss}
# # items() function returns both key & value of dictionary as a list
# dict = sorted(dict.items())
#
# for i in dict:
#     print("%s:%d"%(i[0],i[1]))
#
# def sqt_root(n,p):
#     ''' return the power of the input and the power value '''
#     sqr=n**p
#     return sqr
#
# print(sqt_root(4,4))
#
# print(int().__doc__)  #print  built in int doc
# print(sqt_root.__doc__) # printing my own doc- using doc string ''' '''

# class Car:
#     name = "Car"
#
#     def __init__(self,name = None):
#         self.name = name
#
# honda=Car("Honda")
# print("%s name is %s"%(Car.name,honda.name))
#
# toyota=Car()
# toyota.name="Toyota"
# print("%s name is %s"%(Car.name,toyota.name))
#

# def sum(a='5',b='6'):
#     return int(a) + int(b)
#
# print(sum('4','3'))
#
# sum=lambda x,y:x+y
# print (sum(7,7))

''' Define a function which can print a dictionary where the keys are numbers between 
1 and 20 (both included) andthe values are square of keys.'''
 # O/P - {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400}
# def sqr_dict():
#     dict = {i:i**2 for i in range(1,21)}
#     return dict
#     #return dict.keys() # print only keys
#
# print(sqr_dict())
#
'''Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the first 5 elements in the list.'''
# def list_sqr():
#     lst = ([i**2 for i in range(1,21)][:5])
#     #return lst
#     return tuple(lst)  # to return tuple
# print(list_sqr())

'''write a program to print the first half values in one line and the last half values in one line.'''
# tup= (1,2,3,4,5,6,7,8,9,10)
# lt = int(len(tup)/2)
# print(tup[:lt])
# print(tup[lt:])
# #tup=tuple(i for i in tup if i%2 == 0) # only even tuples
# lst1,lst2=[],[]
# for i in range(0,5):
#     lst1.append(tup[i])
#
# for i in range(5,10):
#     lst2.append(tup[i])
#
# print(lst1)
# print(lst2)

'''Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes",
 otherwise print "No".'''
# def YesNo():
#     strng = input()
#     if strng =='Yes' or strng=='YES' or strng== 'yes':
#         print ("Yes")
#     else:
#         print ("No")
# YesNo()

'''Write a program which can map() to make a list whose elements are square of 
elements in [1,2,3,4,5,6,7,8,9,10]. 2) Use filter() to filter elements of a list.'''
# lst= [1,2,3,4,5,6,7,8,9,10]
# #sqr_map= map(lambda x:x**2,lst) # returns map type object data , squares
# sqr_map= map(lambda x:x**2,filter(lambda x:x%2==0,lst)) # returns even squares only
# sqr_map=(list(sqr_map)) # converting the object into list
# print(sqr_map)

# '''program which can filter() to make a list whose elements are even number between 1 and 20 (both included).'''
# even_filt= filter(lambda x: x%2==0,range(1,21))
# print(list(even_filt))

'''Define a class named American which has a static method called printNationality.'''
# class American():
#     @staticmethod
#     def printNationality():
#         print("American idiot")
#
# call_object=American()
# # call=call_object.printNationality()
# call_object.printNationality() # will not run if static method doesn't decorate printnationality
# American.printNationality() # runs even without decoration by static method
#
# class American():
#     def __init__(self,name1):
#        self.name1=name1
#
#     def president(self):
#         print(self.name.upper())
# class Newyorker(American):
#     def __init__(self,name):
#         self.name=name
#     def governer(self):
#         print(self.name.lower())
#         print(American.president(self)) # inheriting from parent class
#
# obj_country=American("Trump")
# obj_state=Newyorker("Arnold")
#
# # obj_country.president()
# # obj_state.president()
# obj_state.governer()

'''Define a class named Circle which can be constructed by a radius. 
The Circle class has a method which can compute the area.'''
#
# class Circle(object):
#
#     def __init__(self,r,pi=3.14):
#         self.r=r
#         self.pi=pi
#     def area(self):
#         print(self.pi*(self.r**2))
#         # print(area)
#
# circle_obj=Circle(2,3.14)
# circle_obj.area()

'''Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a 
method which can compute the area.'''
# class Rectangle(object):
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
#
#     def area(self):
#         area = self.length * self.breadth
#         return area
#
# obj_rectangle=Rectangle(5,4)
# print(obj_rectangle.area())

# Exception
# def divide():
#     return 5/0
# try:
#     divide()
# except ZeroDivisionError as ze:
#     print("division by zero is wrong !")
# except:
#     print ("any other")
'''Define a custom exception class which takes a string message as attribute.'''

# class Myerror(Exception):
#     '''My own exception class'''
#     def __init__(self,msg):
#         self.msg=msg
# # error=Myerror("something is wrong")
# # print(error)
# num = int(input())
#
# try:
#     if num < 10:
#         raise Myerror("Tnput is less than 10 ")
#     elif num > 10:
#         raise Myerror ("Input is greter than 10")
# except Myerror as me:
#     print("The error raised: " + me.msg)
#
# ''' program to pick username from given email "username@companyname.com" '''
# import re
# class Email(object):
#     def __init__(self,email):
#         self.email=email
#
#     def username(self):
#         #username =self.email.split('@')
#         # pattern = "(\w+)@((\w+\.)+(com))"
#         pattern = "(\w+)@\w+.com"
#         r2 = re.match(pattern,self.email)
#         return(r2.group(1))
#
# call_email=Email('kkunal@gmail.com')
# print(call_email.username())
