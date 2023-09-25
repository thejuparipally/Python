#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 18:06:56 2022

@author: theju
"""

#####################################################
###### Practice Problem 6.21, Page 195 ##############
#####################################################

x=[1,1,2,3,4,4,4,5]

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
    
        






































