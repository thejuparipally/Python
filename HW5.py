#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 18:13:30 2022

@author: theju
"""

# Complete the following homework exercises from the textbook:

# 5.12, 5.14, 5.16, 5.18, 5.23, 5.30, 5.32

# Please use the techniques and concepts that we have covered in Chapters 2 through 5 to answer the questions. No use of recursive functions is allowed. Submit your assignment in a single .py file that uses comments to clearly label each problem. Contact the instructor ASAP if you have any questions.

#####################################################
##### Practice Problem 5.12, Page 155 ###############
#####################################################

# Implement function test() that takes as input one integer and prints 'Negative',
# 'Zero', or 'Positive' depending on its value.
#    >>> test(-3)
#    Negative
#    >>> test(0)
#    Zero
#    >>> test(3)
#    Positive

def test(n):
    if n<0:
        print ("Negative")
    elif n>0:
        print ("Positive")
    else:
        print ("Zero")

test(-3)
test(0)
test(3)

#####################################################
##### Practice Problem 5.14, Page 155 ###############
#####################################################

# Write function mult3() that takes as input a list of integers and prints only the multiples of 3, one per line.
#    >>> mult3([3, 1, 6, 2, 3, 9, 7, 9, 5, 4, 5])
#    3
#    6
#    3
#    9 
#    9

def mult3(lst):
    for num in lst:
        if num % 3 == 0:
           print (num)
           
mult3([3, 1, 6, 2, 3, 9, 7, 9, 5, 4, 5])

#####################################################
##### Practice Problem 5.16, Page 156 ###############
#####################################################

# Implement function indexes() that takes as input a word (as a string) and a one- character letter (as a string) and returns a list of indexes at which the letter occurs in the word.
# >>> indexes('mississippi', 's') 
# [2, 3, 5, 6]
# >>> indexes('mississippi', 'i') 
# [1, 4, 7, 10]
# >>> indexes('mississippi', 'a') 
# []

def indexes(word, char):
    lst= []
    length=len(word)
    for i in range(0,length):
            if word[i] == char:
                lst.append(i)
    return lst
        
indexes('mississippi', 's') 
indexes('mississippi', 'i') 
indexes('mississippi', 'a') 

#####################################################
##### Practice Problem 5.18, Page 156 ###############
#####################################################

# Implement function four_letter() that takes as input a list of words (i.e.,strings) and returns the sublist of all four letter words in the list.
# >>> four_letter(['dog', 'letter', 'stop', 'door', 'bus', 'dust']) 
# ['stop', 'door', 'dust']

def four_letter(lst):
    fourletter= [] 
    for i in lst:
        if len(i)==4:
            fourletter.append(i)
    return fourletter

four_letter(['dog', 'letter', 'stop', 'door', 'bus', 'dust']) 
            
#####################################################
##### Practice Problem 5.23, Page 157 ###############
#####################################################

# Write function pay() that takes as input an hourly wage and the number of hours an employee worked in the last week. The function should compute and return the employee’s pay. Overtime work should be paid in this way: Any hours beyond 40 but less than or equal 60 should be paid at 1.5 times the regular hourly wage. Any hours beyond 60 should be paid at 2 times the regular hourly wage.
#    >>> pay(10, 35)
#    350
#    >>> pay(10, 45)
#    475.0
#    >>> pay(10, 61)
#    720.0

def pay(wage,hours):
    if hours < 40:
        pay= hours * wage
    elif hours <= 60: 
        pay = (wage * 40) + ((1.5 * wage) * (hours - 40))
    else:
        pay= ( wage * 40) + ((1.5 * wage * 20)) + ((2 * wage) * (hours - 60)) 
    return pay

pay(10, 35)
pay(10, 45)
pay(10, 61)

#####################################################
##### Practice Problem 5.30, Page 158 ###############
#####################################################

# Develop the function many() that takes as input the name of a file in the current directory (as a string) and outputs the number of words of length 1, 2, 3, and 4. Test your function on file sample.txt.
# >>> many('sample.txt') 
# Words of length 1 : 2 
# Words of length 2 : 5 
# Words of length 3 : 1 
# Words of length 4 : 10

def many(file):
    infile=open(file)
    string=infile.read()
    infile.close()
    periods = str.maketrans ("!,.:;?", 6*" ")
    string=string.translate(periods)
    words = string.split()
    len1= []
    len2=[]
    len3=[]
    len4=[]
    for word in words:
        if len(word)==1:
            len1.append(word)
        elif len(word) == 2:
            len2.append(word)
        elif len(word) == 3:
            len3.append(word)
        elif len(word) == 4:
            len4.append(word) 
    print ("Words of length 1 : " +str(len(len1))+ "\nWords of length 2 : " +str(len(len2))+ "\nWords of length 3 : " +str(len(len3))+ "\nWords of length 4 : " +str(len(len4)))       

many('sample.txt') 

#####################################################
##### Practice Problem 5.32, Page 159 ###############
#####################################################

# Implement function fib() that takes a nonnegative integer n as input and returns the nth Fibonacci number.
# >>> fib(0)
# 1
# >>> fib(4)
# 5
# >>> fib(8) 
# 34

# a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. 
# The simplest is the series 1, 1, 2, 3, 5, 8


def fib(n):
    if n<0:
        print (" Enter a non negative number")
    elif n == 0 or n == 1:
        print ("1")
    elif n == 2:
        print ("2")
    elif n>2:
        for i in range(n): 
            num2= n-2
            num1= n-1
            num=num1+num2
        return num
    
fib(0)
fib(4)
fib(8) 

        










































