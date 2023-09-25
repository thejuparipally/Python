#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 18:06:29 2022

@author: theju
"""

# Chapter 6:
    
# [] - list
# () - tuple
# {} - dictionary

# key must be unique

#####################################################
##### Practice Problem 6.1, Page 168 ###############
#####################################################

# Write a function birthState() that takes as input the full name of a recent U.S. president (as a string) and returns his birth state. You should use this dictionary to store the birth state for each recent president:
# {'Barack Hussein Obama II':'Hawaii',
# 'George Walker Bush':'Connecticut',
# 'William Jefferson Clinton':'Arkansas', 'George Herbert Walker Bush':'Massachussetts', 'Ronald Wilson Reagan':'Illinois',
# 'James Earl Carter, Jr':'Georgia'}
# >>> birthState('Ronald Wilson Reagan') 'Illinois'

def birthState(name):
    pres= {'Barack Hussein Obama II':'Hawaii', 
      'George Walker Bush':'Connecticut', 
      'William Jefferson Clinton':'Arkansas', 
      'George Herbert Walker Bush':'Massachussetts', 
      'Ronald Wilson Reagan':'Illinois', 
      'James Earl Carter, Jr':'Georgia'}   #key mumst be unique. Does it work if key,values were reversed? Flip keys, values -- > values, keys. But it might work now, but if there are more names with same states then the key is not unique anymore.
    if name in pres:
        return pres[name]
    else:
        return " Name not in the list"

birthState("Barack Hussein Obama II")

#####################################################
###### Practice Problem 6.2, Page 169 ###############
#####################################################
            
# Implement function rlookup() that provides the reverse lookup feature of a phone book.
# Your function takes, as input, a dictionary representing a phone book. In the dictionary, phone numbers (keys) are mapped to individuals (values). 
# Your function should provide a simple user interface through which a user can enter a phone number and obtain the first and last name of the individual assigned that number.
# >>> rphonebook = {'(123)456-78-90':['Anna','Karenina'], '(901)234-56-78':['Yu', 'Tsun'],'(321)908-76-54':['Hans', 'Castorp']} 
# >>> rlookup(rphonebook)
# Enter phone number in the format (xxx)xxx-xx-xx: (123)456-78-90 ('Anna', 'Karenina')
# Enter phone number in the format (xxx)xxx-xx-xx: (453)454-55-00 The number you entered is not in use.
#         Enter phone number in the format (xxx)xxx-xx-xx:


def rlookup(pbook):
    pnum= input("Enter phone number in the format (xxx)xxx-xxxx: ")
    if pnum in pbook:
        return pbook[pnum]
    else:
        return "The number is not in the phonebook"
        
rphonebook = {'(123)456-7890':['Anna','Karenina'], '(901)234-5678':['Yu', 'Tsun'],'(321)908-7654':['Hans', 'Castorp']} 
rlookup(rphonebook)

#####################################################
###### Practice Problem 6.4, Page 175 ###############
#####################################################

# Implement function wordcount() that takes as input a text—as a string— and prints the frequency of each word in the text. You may assume that the text has no punctuation and words are separated by blank spaces.
# >>> text = 'all animals are equal but some \ animals are more equal than others'
# >>> wordCount(text)
# all appears 1 time.
#    animals  appears 2 times.
#    some     appears 1 time.
#    equal    appears 2 times.
#    but      appears 1 time.
#    are      appears 2 times.

def wordCount(sen):
    words= sen.split()
    counter= {}
    for word in words:
        if word in counter:
            counter [word] +=1 
        else:
            counter[word] = 1
    u_word = counter.keys()
    for word in u_word:
        print ("{}:\t appears {} time(s)".format(word,counter[word]))
        #print ("{:8} appears {} time(s)".format(word,counter[word]))
        
text = 'all animals are equal but some \ animals are more equal than others'
wordCount(text) 

#if counter[word] ==1 then print with times without s and if >1 then print with times

#####################################################
###### Practice Problem 6.7, Page 183 ###############
#####################################################

# Write a function encoding() that takes a string as input and prints the ASCII code—in decimal, hex, and binary notation—of every character in it.
# >>> encoding('dad')
# Char Decimal Hex Binary
#  d     100   64  1100100
#  a     97   61  1100001
#  d     100   64  1100100

def encoding(s1):
    print("Char Decimal")
    for char in s1:
        print('{}    {:7}'.format(char, ord(char)))
        
#####################################################
###### Practice Problem 6.8, Page 183 ###############
#####################################################
    
# Write function char(low, high) that prints the characters corresponding to ASCII deci- mal codes i for all values of i from low up to and including high.
#    >>> char(62, 67)
#    62 : >
#    63 : ?
#    64 : @
#    65 : A
#    66 : B
#    67 : C

def char(low,high):
    for i in range(low,high+1):
        print ("{} : {}".format (i, chr(i)))

char(62, 67)

# NOTES on random module:
    
# random.randrange(1,7) #die six sided random number
# random.uniform(0,1)  

# lst = [1,2,3,4,5]
# random.shuffle(lst)
# lst

# random.choice(lst)
# random.sample(lst, 3) #pick random 3 sample values

#####################################################
###### Practice Problem 6.9, Page 187 ###############
#####################################################

# Implement function guess() that takes as input an integer n and implements a simple, interactive number guessing game.
# The function should start by choosing a random num- ber in the range from 0 up to but not including n. 
# The function will then repeatedly ask the user to guess the chosen number; When the user guesses correctly, the function should print a 'You got it.' message and terminate. 
# Each time the user guesses incorrectly, the function should help the user by printing message 'Too low.', or 'Too high.'.
#    >>> guess(100)
#    Enter your guess: 50
#    Too low.
#    Enter your guess: 75
#    Too high.
#    Enter your guess: 62
#    Too high.
#    Enter your guess: 56
#    Too low.
#    Enter your guess: 59
#    Too high.
#    Enter your guess: 57
#    You got it!

import random
def guess(n):
    val = random.randrange (0,n)
    while True:
        prompt = eval(input("Enter your guess: "))
        if prompt == val:
            print ("You got it!")
            break
        elif prompt < val:
            print ("Tow low.")
        else:
            print ("Too high!")













































