#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 22:30:12 2022

@author: theju
"""
#Assignment 2

#####################################################
############## Homework Problem 3.1 #################
#####################################################

# Complete the following homework exercises. Submit your assignment in a single .py file that uses comments to clearly label each problem. Contact the instructor ASAP if you have any questions.

# HW 3.1) Assume a, b, and c have been defined as shown:
# a, b, c = 7, 8, 9
a, b, c = 7, 8, 9
# Within your Python script, write if statements that print 'OK' if:
# (a) a is less than b.
if a < b:
    print ("OK")
# (b) c is less than b.
if c < b:
    print ("OK")
# (c) The sum of a and b is equal to c.
if (a + b)== c:
    print ("OK")
# (d) The sum of the squares a and b is equal to c squared.
if (a**2 + b**2)== c**2:
    print ("OK")

# HW 3.2) Repeat the previous problem with the additional requirement that 'NOT OK' is printed
# if the condition is false.

# (a) a is less than b.
if a < b:
    print ("OK")
else:
    print ("NOT OK")
# (b) c is less than b.
if c < b:
    print ("OK")
else:
        print ("NOT OK")
# (c) The sum of a and b is equal to c.
if (a + b)== c:
    print ("OK")
else:
        print ("NOT OK")
# (d) The sum of the squares a and b is equal to c squared.
if (a**2 + b**2)== c**2:
    print ("OK")
else:
    print ("NOT OK")
    
# HW 3.3) Write a for loop that iterates over a list of numbers of a list named 
# lst3 and prints the odd numbers in the list. 
# For example, if lst3 is [2, 3, 4, 5, 6, 7, 8, 9], then the numbers 3, 5, 7, and 9 should be printed.

lst3 = [2, 3, 4, 5, 6, 7, 8, 9]
for num in lst3:
    if num % 2 != 0:
        print (num)
    
# HW 3.4) Write a for loop that iterates over a list of numbers named lst34 and prints the numbers in the
# list whose square is divisible by 9. 
# For example, if lst34 is [2, 3, 4, 5, 6, 7, 8, 9] then the numbers 3, 6 and 9 should be printed.

lst34= [2, 3, 4, 5, 6, 7, 8, 9] 
for num in lst3:
    if (num**2) % 9 == 0:
        print (num)
        
# HW 3.5) Implement a program that requests a list of words from the user and then prints each word in the list that is not contained in 'another'
# For example:
# Enter list of words: ['her','another','him','other','not',’is’]
# him
# is

list= eval(input("Enter list of words: "))
for word in list:
    if word not in 'another':
        print(word)
        

# HW 3.6) Implement a program that requests a positive integer n from the user and prints the
# first five multiples of n (n*0, n*1, n*2, n*3, and n*4).
# For example:
# Enter n: 9
# 0
# 9
# 18
# 27
# 36

n= eval(input("Enter a positive integer n: "))
for i in range(0,5):
    print(n*i)

# HW 3.7) Implement a program that requests a positive integer n and prints on the screen all the
# Positive integer divisors of n. Note: 0 is not a divisor of any integer, and n divides itself.
# For example:
# Enter n: 49
# 1
# 7
# 49

n= eval(input("Enter n: "))
for i in range(1,n+1):
    if((n%i) == 0):
        print(i)

# HW 3.8) Implement a program that requests four numbers (integer or floating-point) from the
# user. Your program should compute the sum of the first three numbers and compare the
# sum to the fourth number. If they are equal, your program should print 'Equal' on the
# screen.
# >>> 
# Enter first number: 5.5
# Enter second number: 3
# Enter third number: 4
# Enter last number: 12.5
# Equal

num1= eval(input("Enter first number: "))
num2= eval(input("Enter second number: "))
num3= eval(input("Enter third number: "))
num4= eval(input("Enter last number: "))
sum= num1 +num2 +num3
if (sum == num4):
    print ("Equal")














