#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 19:44:24 2022

@author: theju
"""

# Complete the following homework exercises from the textbook (found on pages 124-125):

# 4.22, 4.23, 4.24, 4.25, 4.27, 4.29, 4.30, 4.31, 4.32

# On problem #30, don't worry about the s at the end of "students" for grades that contain only 1 value. Just let them all say "students".

# Homework solutions may only utilize techniques and methods that have been covered in Chapters 1-4 of the textbook. Any other methods that are utilized may be subject to reduced or no credit given for that problem or the assignment.

# Submit your assignment in a single .py file that uses comments to clearly label each problem. Contact the instructor ASAP if you have any questions.

#####################################################
##### Practice Problem 4.22, Page 124 #################
#####################################################

# Write a function month() that takes a number between 1 and 12 as input and returns the three-character abbreviation of the corresponding month. Do this without using an if statement, just string operations. 
# Hint: Use a string to store the abbreviations in order.
# 'Jan'
# >>> month(11)
# 'Nov'

def month(n):
    for i in range (1,13):
        str= "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec"
        mon=str.split()
    return (mon[n-1])

month(12)
        
#####################################################
##### Practice Problem 4.23, Page 124 #################
#####################################################

# Write a function average() that takes no input but requests that the user enter a sentence. Your function should return the average length of a word in the sentence.
# >>> average()
# Enter a sentence: A sample sentence
# 5.0


def average():
    a=0
    s = input("Enter a sentence: ")
    sen_list= s.split(" ")
    for i in sen_list:
        a = a + len(i)
    average= a/(len(sen_list))
    return (average)

average()
        
#####################################################
##### Practice Problem 4.24, Page 124 #################
#####################################################

# Implement function cheer() that takes as input a team name (as a string) and prints a cheer as shown:
# >>> cheer('Huskies')
# How do you spell winner?
# I know, I know!
# HUSKIES!
# And that's how you spell winner! Go Huskies!
 
def cheer(name):
    char= name.upper()
    print ("How do you spell winner?\nI know, I know!")
    for i in char:
        print(i,end=" ")
    print("!\nAnd that's how you spell winner!\nGo "+name+"!")
    
cheer("Huskies")

#####################################################
##### Practice Problem 4.25, Page 124 #################
#####################################################

# Write function vowelCount() that takes a string as input and counts and prints the number of occurrences of vowels in the string.
# >>> vowelCount('Le Tour de France')
# a, e, i, o, and u appear, respectively, 1, 3, 0, 1, 1 times.

def vowelCount(string):
    sen=string.lower()   #Since its cases senstive, converting the inputted string into lowercase
    a=sen.count("a")
    e=sen.count("e")
    i=sen.count("i")
    o=sen.count("o")
    u=sen.count("u")
    print("a, e, i, o, and u appear, respectively, {}, {}, {}, {}, {}".format(a,e,i,o,u)+ " times.")

vowelCount('Le Tour de France')

#####################################################
##### Practice Problem 4.27, Page 124 #################
#####################################################

# Write a function fcopy() that takes as input two file names (as strings) and copies
# the content of the first file into the second.
# >>> fcopy('example.txt','output.txt')
# >>> open('output.txt').read()
# 'The 3 lines in this file end with the new line character.\n\n
# There is a blank line above this line.\n'

def fcopy(file1, file2):
    infile= open(file1)
    s1 = infile.read()
    infile.close()
    outfile= open(file2, 'w')
    outfile.write(s1)
    outfile.close()
    
fcopy('example.txt','output.txt')
open('output.txt').read()
    

#####################################################
##### Practice Problem 4.29, Page 125 #################
#####################################################

# Write a function stats() that takes one input argument : the name of a text file.The function should print, on the screen, the number of lines, words, and characters in the file; your function should open the file only once.
# >>> stats('example.txt') 
# line count: 3
# word count: 20 
# character count: 98

def stats(file):
    infile=open(file)
    f=infile.read()
    infile.close()
    character = f.count("")
    word = f.count(" ") + 2          #Adding 2 to take into account the first word and last word of the file 
    line = f.count("\n") + 1         #Adding 1 to take into account the first sentence in the file
    print("line count: "+str(line)+ "\nword count: "+str(word)+ "\ncharacter count: "+str(character))
    
stats('Duplicates.txt')  

#####################################################
##### Practice Problem 4.30, Page 125 #################
#####################################################

# Implement function distribution() that takes as input the name of a file (as a string). This one-line file will contain letter grades separated by blanks. Your function should print the distribution of grades, as shown.
# >>> distribution('grades.txt')
# 6 students got A
# 2 students got A-
# 3 students got B+
# 2 students got B
# 2 students got B-
# 4 students got C
# 1 student  got C-
# 2 students got F

def distribution(file):
    infile=open(file)
    grade=infile.read()
    infile.close()
    An = grade.count("A-")
    Bp = grade.count("B+")
    Bn = grade.count("B-")
    Cn = grade.count("C-")
    A = grade.count("A") - An          #grade.count(A) takes A + A- values. To get only grade A, deducted A- values from count of A
    B = grade.count("B") - Bp - Bn     #grade.count(B) takes B + B- + B+ values. To get only grade B, deducted B- and B+ values from count of B
    C = grade.count("C") - Cn          #grade.count(C) takes C + C- values. To get only grade C, deducted A- values from count of C
    F = grade.count("F")
    print("{} students got A\n{} students got A-\n{} students got B+\n{} students got B\n{} students got B-\n{} students got C\n{} students got C-\n{} students got F".format(A,An,Bp,B,Bn,C,Cn,F))
    
distribution('grades.txt')

#####################################################
##### Practice Problem 4.31, Page 125 #################
#####################################################

# Implement function duplicate() that takes as input the name (a string) of a file in the current directory and returns True if the file contains duplicate words and False otherwise.
# >>> duplicate('Duplicates.txt') True
# >>> duplicate('noDuplicates.txt') False

def duplicate(file):
    infile=open(file)
    string=infile.read()
    infile.close()
    periods = str.maketrans ("!,.:;?", 6*" ")
    string=string.translate(periods)
    words = string.split()
    for word in words:
        if words.count(word) > 1:
            return True
    else:
        return False
                         
duplicate('Duplicates.txt') 
duplicate('noDuplicates.txt')    

#####################################################
##### Practice Problem 4.32, Page 125 #################
#####################################################

# The function censor() takes the name of a file ( a string) as input.The function should open the file, read it, and then write it into file censored.txt with this modification: Every occurrence of a four-letter word in the file should be replaced with string 'xxxx'.
# >>> censor('example.txt')
# Note that this function produces no output, but it does create file censored.txt in the current folder.

def censor(file):
    infile=open(file)
    modify=infile.read()
    infile.close()
    word = modify.split()
    for i in word:
        if len(i)==4:
            modify = modify.replace(i, "****")
    outfile = open("censored.txt",'w')
    outfile.write(modify)
    outfile.close()
    
censor('example.txt')

#right solution:   
                   
def censor(file):
    infile=open(file)
    modify=infile.read()
    infile.close()
    word = modify.split()
    modify= modify.replace(".", " .")
    for i in word:
        if len(i)==4:
            modify = modify.replace(" " +i+ " ", " **** ")
    modify= modify.replace(" .", ".")
    outfile = open("censored.txt",'w')
    outfile.write(modify)
    outfile.close()
    
censor('example.txt')
              
    
     
    














