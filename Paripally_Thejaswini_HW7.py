#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 19:54:38 2022

@author: theju
"""

def lst_count(x):
    n=0
    for i in x:
        n +=1
    return n

def lst_sum(x):
    lsum=0
    for i in x:
        lsum += i
    return lsum
    
def lst_mean(x):
    return lst_sum(x)/lst_count(x)

def lst_min(x):
    lmin=x[0]
    for i in x:
        if i < lmin:
            lmin = i
    return lmin

def lst_max(x):
    lmax=x[0]
    for i in x:
        if i>lmax:
            lmax=i
    return lmax
            
def lst_range(x):
    return lst_max(x) - lst_min(x)

def lst_median(x):
    x.sort()
    n=lst_count(x)
    if n % 2 == 0:
        i = int(n/2)
        middle_values = [x[i], x[i-1]]
        return lst_mean(middle_values)
    else:
        i= int((n-1)/2)
        return x[i]

def lst_variance(x):
    x_bar= lst_mean(x)
    sq_diff=[]
    for val in x:
        sq_diff.append((val - x_bar)**2)
    num = lst_sum(sq_diff)
    return num/ (lst_count(x)-1)
        
def lst_stdev(x):
    return lst_variance(x)**0.5


def lm():
    
    x = []
    y = []
    x2 = []
    y2 = []
    xy = []
    cordinates = []
    numofcordinates = eval(input("How many data points (ordered pairs(x,y)) so you plan to enter? (maximum of 20): "))
    if numofcordinates > 20: 
        print ("Enter a number less than 20")
    else:
        for i in range(numofcordinates):
            x_cordinates= eval(input ("Enter the data point x: "))
            y_cordinates= eval(input ("Enter the data point y: "))
            x.append(x_cordinates)
            y.append(y_cordinates)
            

            
            x2_cordinates= (x_cordinates)**2
            y2_cordinates= (y_cordinates)**2
            xy_cordinates= (x_cordinates) * (y_cordinates)
            
            xy.append(xy_cordinates)
            x2.append(x2_cordinates)
            y2.append(y2_cordinates)
            
        cordinates.append(x)
        cordinates.append(y)

    r = ((lst_count(x) *lst_sum(xy))-(lst_sum(x) * lst_sum(y))) / ((((lst_count(x) * lst_sum(x2))-(lst_sum(x))**2)*((lst_count(x) * lst_sum(y2))-(lst_sum(y))**2))**0.5)
    
    m = r * (lst_stdev(y)/ lst_stdev(x)) 
    
    b = lst_mean(y) - (m * lst_mean(x))
    
    print ("\nData points as list [x],[y] : {}".format(cordinates))
    print ("The correlation coefficient for the data set is : {}".format(r))
    print ("The least-squares regression line for your data set is : y = {}x + {}".format (m,b))
    
    
def summary(x):
    print ("The mean for the list of values is : {} ".format(lst_mean(x)))
    print ("The median for the list of values is: {} ".format(lst_median(x)))
    print ("The standard deviation for the list of values is: {} ".format(lst_stdev(x)))
    print ("The variance for the list of values is: {} ".format(lst_variance(x)))
    print ("The range for the list of values is: {} ".format(lst_range(x)))
    print ("The minimum for the list of values is: {} ".format(lst_min(x)))
    print ("The maximum for the list of values is: {} ".format(lst_max(x)))
    print ("The sum for the list of values is: {} ".format(lst_sum(x)))
    print ("The count for the list of values is: {} ".format(lst_count(x)))
    
    
    
    

    




    
    

















    
    
    
    








































