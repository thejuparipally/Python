#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 20:06:48 2022

@author: Theju
"""

# Complete the following homework exercises:

# HW 3.9) Implement function reverse_string() that takes as input a string and returns the string with its characters reversed.
# >>> reverse_string('chad')
# 'dahc'
# >>> reverse_string('birger')
# 'regrib'

def reverse_string(string):  
    temp = ""  
    for i in string:  
        temp = i + temp  
    return temp 

# HW 3.10) Implement function pay() that takes as input two arguments: an hourly wage and the
# number of hours an employee worked in the last week. Your function should compute and
# return the employee’s pay. Any hours worked beyond 40 is overtime and should be paid at
# 1.5 times the regular hourly wage.
# >>> pay(10, 35)
# 350
# >>> pay(10, 45)
# 475.0

def pay(wage,hours):
    if hours > 40:
        overtime = (wage * 40) + ((1.5 * wage) * (hours - 40))
        return overtime
    else:
        return hours * wage 
   
# HW 3.11) The probability of getting n heads in a row when tossing a fair coin n times is 2^-n.
# Implement function prob() that takes a nonnegative integer n as input and returns the
# probability of n heads in a row when tossing a fair coin n times.
# >>> prob(1)
# 0.5
# >>> prob(2)
# 0.25

def prob(n):
    if n > 0:
        prob= 2 ** -n
        return prob

# HW 3.12) Implement function points() that takes as input four numbers x1, y1, x2, y2 that
# are the coordinates of two points (x1; y1) and (x2; y2) in the plane. Your function should
# compute:
# • The slope of the line going through the points, unless the line is vertical
# • The distance between the two points
# Your function should print the computed slope and distance in the following format. If the
# line is vertical, the value of the slope should be string 'infinity'. Note: Make sure you
# convert the slope and distance values to a string before printing them.
# >>> points(0, 0, 1, 1)
# The slope is 1.0 and the distance is 1.41421356237
# >>> points(0, 0, 0, 1)
# The slope is infinity and the distance is 1.0

def points(x1,y1,x2,y2):
    import math
    if(x1-x2 == 0): 
        slope = "infinity"
        distance= str(math.sqrt(((x2-x1)**2) + ((y2-y1)**2)))
        print ("The slope is infinity and the distance is " +distance)
    else:
        slope = str((y2-y1)/(x2-x1))
        distance= str(math.sqrt(((x2-x1)**2) + ((y2-y1)**2)))
        print ("The slope is " + slope + " and the distance is " +distance)


# HW 3.13) Write function lastF() that takes as input two strings of the form 'FirstName' and
# 'LastName', respectively, and returns a string of the form 'LastName, F.'. (Only the
# initial should be output for the first name.)
# >>> lastF('Chad', 'Birger')
# 'Birger, C.'

def lastF(FirstName, LastName):
    name = LastName.capitalize() + " , " + (FirstName.capitalize())[0] + '.'
    return name

# HW 3.14) Write function ppsi() that takes as input two numbers price and diameter. These will represent the price of a circular shaped pizza and the diameter of the pizza. The function should return the price per square inch of the pizza. 
# >>> ppsi(10, 9)
# 0.15719006725125467
# >>> ppsi(5, 5)
# 0.25464790894703254

def ppsi(price, diameter):
    import math
    radius = diameter/2 
    area = math.pi * (radius**2)
    ppsi= price/ area
    return ppsi

# Submit your assignment in a single .py file that uses comments to clearly label each problem. Contact the instructor ASAP if you have any questions.






































