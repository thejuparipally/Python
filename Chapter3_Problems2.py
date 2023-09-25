#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 18:01:25 2022

@author: theju
"""

#To call the function you type the function name with ()
# You can globally call import math first before starting anything else so it applies for all instead of under each question.

#####################################################
##### Practice Problem 3.8, Page 68 #################
#####################################################

# 3.8. Define, directly in the interactive shell, function perimeter() that takes, as input, the ra- dius of a circle (a nonnegative number) and returns the perimeter of the circle. A sample usage is:
#    >>> perimeter(1)
#    6.283185307179586
#    >>> perimeter (2)
#    12.566370614359172
# Remember that you will need the value of ⇡ (defined in module math) to compute the perimeter.

r = eval(input("Enter the radius of the circle r: "))
def perimeter(r):
    import math
    p= 2 * math.pi * r
    return p
print (perimeter(r))

#####################################################
##### Practice Problem 3.9, Page 69 #################
#####################################################

# 3.9. Implement function average() that takes two numbers as input and returns the average of the numbers. You should write your implementation in a module you will name average.py. A sample usage is:
#    >>> average(1,3)
#    2.0
#    >>> average(2, 3.5)
#    2.75

num1= eval(input("Enter the first number: "))
num2= eval(input("Enter the second number: "))
def average(num1,num2):
    avg = (num1+num2)/2
    return avg
print (average(num1,num2))

#####################################################
##### Practice Problem 3.10, Page 69 #################
#####################################################

# 3.10. Implement function noVowel() that takes a string s as input and returns True if no char- acter in s is a vowel, and False otherwise (i.e., some character in s is a vowel).
# >>> noVowel('crypt') True
# >>> noVowel('cwm') True
# >>> noVowel('car') False

def noVowel(s):
    vowels = "aeiouAEIOU"
    for letter in s:
        if letter in vowels:
            return False
    return True

#Another Way

# s = eval(input("Enter the string s: "))
# def noVowel(s):
#     vowels = "aeiouAEIOU"
#     for char in s:
#         if char in vowels:
#             return False
#     return True
# print (noVowel(s))

#####################################################
##### Practice Problem 3.11, Page 69 #################
#####################################################

# 3.11. Implement function allEven() that takes a list of integers and returns True if all integers in the list are even, and False otherwise.
#    >>> allEven([8, 0, -2, 4, -6, 10])
#    True
#    >>> allEven([8, 0, -1, 4, -6, 10])
#    False

def allEven(list):
    for num in list:
        if num % 2 != 0:
            return False
    return True


#####################################################
##### Practice Problem 3.12, Page 71 #################
#####################################################

# 3.12. Write function negatives() that takes a list as input and prints, one per line, the negative values in the list. The function should not return anything.
#    >>> negatives([4, 0, -1, -3, 6, -9])
#    -1
#    -3
#    -9

def negatives(lst_num):
    for num in lst_num:
        if num < 0:
            print (num)

#####################################################
##### Practice Problem 3.13, Page 73 #################
#####################################################

# 3.13. Add appropriate docstrings to functions average() and negatives() from Practice Prob- lems 3.9 and 3.12. Check your work using the help() documentation tool. You should get, for example:
#    >>> help(average)
#    Help on function average in module __main__:
#    average(x, y)
#        returns average of x and y

help(average)
average (1,3)

#####################################################
##### Practice Problem 3.15, Page 78 #################
#####################################################

# Suppose a nonempty list team has been assigned. Write a Python statement or statements that swap the first and last value of the list. So, if the original list is:
# >>> team = ['Ava', 'Eleanor', 'Clare', 'Sarah'] then the resulting list should be:
# >>> team
# ['Sarah', 'Eleanor', 'Clare', 'Ava']

team = ['Ava', 'Eleanor', 'Clare', 'Sarah']
team[0],team[-1]=team[-1],team[0]
print (team)

#####################################################
##### Practice Problem 3.16, Page 81 #################
#####################################################

# Implement function swapFL() that takes a list as input and swaps the first and last ele- ments of the list. You may assume the list will be nonempty. The function should not return anything.
# >>> ingredients = ['flour', 'sugar', 'butter', 'apples'] >>> swapFL(ingredients)
# >>> ingredients
# ['apples', 'sugar', 'butter', 'flour']

def swapFL(lst_swap):
    if len(lst_swap) > 1:
        lst_swap[0],lst_swap[-1]=lst_swap[-1],lst_swap[0]
        #print (lst_swap)























