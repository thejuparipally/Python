#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 18:07:04 2022

@author: theju
"""

#####################################################
##### Practice Problem 4.1, Page 95 #################
#####################################################

# Start by executing the assignment:
# s = '0123456789'
s = '0123456789'
# Now write expressions using string s and the indexing operator that evaluate to: 
# (a) '234'
s[2:5]
# (b) '78'
s[7:9]
s[-3:-1]
# (c) '1234567'
s[1:8]
# (d) '0123' 
s[7:]
# (e) '789'
s[-3:]
s[7:]

#####################################################
##### Practice Problem 4.2, Page 98 #################
#####################################################

# Assuming that variable forecast has been assigned string 'It will be a sunny day today'
forecast = "It will be a sunny day today"
# write Python statements corresponding to these assignments:
# (a) To variable count,the number of occurrences of string 'day' in string forecast.
count= forecast.count("day")
# (b) To variable weather,the index where substring 'sunny' starts.
weather= forecast.find("sunny")
# (c) To variable change, a copy of forecast in which every occurrence of substring 'sunny' is replaced by 'cloudy'.
change= forecast.replace("sunny", "cloudy")

#####################################################
##### Practice Problem 4.3, Page 99 #################
#####################################################

# Write a statement that prints the values of variables last, first, and middle in one line, separated by a horizontal tab character. (The Python escape sequence for the horizontal tab character is \t.) If the variables are assigned like this:
# >>> last = 'Smith' >>> first = 'John' >>> middle = 'Paul'
last = 'Smith'
first = 'John'
middle = 'Paul'
# the output should be:
#    Smith   John    Paul
print(last, first, middle, sep= "\t ")

#####################################################
##### Practice Problem 4.4, Page 100 #################
#####################################################

# Write function even() that takes a positive integer n as input and prints on the screen all numbers between, and including, 2 and n divisible by 2 or by 3, using this output format:
#    >>> even(17)
#    2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16,
def even(n):
    if n > 1:
        for i in range(2, n+1):
            if i % 2 == 0 or i % 3 == 0:
                print(i, end= ",")
    
#####################################################
##### Practice Problem 4.5, Page 102 #################
#####################################################

# Assume variables first, last, street, number, city, state, zipcode have already been assigned. Write a print statement that creates a mailing label:
#    John Doe
#    123 Main Street
#    AnyCity, AS 09876
# assuming that:
# >>> first = 'John'
# >>> last = 'Doe'
# >>> street = 'Main Street'
# >>> number = 123
# >>> city = 'AnyCity'
# >>> state = 'AS'
# >>> zipcode = '09876'

first = 'John'
last = 'Doe'
street = 'Main Street' 
number = 123
city = 'AnyCity'
state = 'AS'
zipcode = '09876'

address= "{} {}\n{} {}\n{}, {} {}"
print(address.format(first,last,number,street,city,state,zipcode))

print(first + " " + last + "\n" +str(number) + " " + street + "\n" +city+ "," +state+ " " +zipcode)

#####################################################
##### Practice Problem 4.6, Page 105 #################
#####################################################

# Implement function roster() that takes a list containing student information and prints out a roster, as shown below. The student information, consisting of the student’s last name, first name, class, and average course grade, will be stored in that order in a list. Therefore, the input list is a list of lists. Make sure the roster printed out has 10 slots for every string value and 8 for the grade, including 2 slots for the decimal part.
# >>> students = []
# >>> students.append(['DeMoines', 'Jim', 'Sophomore', 3.45]) >>> students.append(['Pierre', 'Sophie', 'Sophomore', 4.0]) >>> students.append(['Columbus', 'Maria', 'Senior', 2.5]) >>> students.append(['Phoenix', 'River', 'Junior', 2.45]) >>> students.append(['Olympis', 'Edgar', 'Junior', 3.99]) >>> roster(students)
# Last First Class Average Grade
# DeMoines Jim Sophomore 3.45
# Pierre Sophie Sophomore 4.00
# Columbus Maria Senior 2.50
# Phoenix River Junior 2.45
# Olympia Edgar Junior 3.99

students = []
students.append(['DeMoines', 'Jim', 'Sophomore', 3.45])
students.append(['Pierre', 'Sophie', 'Sophomore', 4.0])
students.append(['Columbus', 'Maria', 'Senior', 2.5]) 
students.append(['Phoenix', 'River', 'Junior', 2.45])
students.append(['Olympis', 'Edgar', 'Junior', 3.99])

def roster(lst):
    print('Last    First     Class    Average Grade')
    for ele in lst:
        print("{:10}{:10}{:10}{:8.2f}".format(ele[0], ele[1], ele[2], ele[3]))
        
roster(students)

#INFILE NOTES

infile = open("example.txt") #opens the file in anaconda with mode read as default
s1 = infile.read()           #stores the file content in string s1
s2=infile.read(10)           #reads and stores the first 10 characters in the file including space in s2 from the cursor pointer
s3=s1[5:15]                  #using slicing operator we can print character from index 5 to 15
s4=infile.readline()         #reads the line till the first end of the file that is \n. Read file infile until (and including) the new line character or until end of file, whichever is first, and return characters read as a string
s5=infile.readlines()        # Read file infile until the end of the file and return the characters read as a list lines
infile.close()               #closes the connection to the file
        
#####################################################
##### Practice Problem 4.8, Page 113 #################
#####################################################  

# Write function stringCount() that takes two string inputs—a file name and a target string— and returns the number of occurrences of the target string in the file.
# >>> stringCount('example.txt', 'line') 4

def stringCount(file,target):
    infile= open(file)
    s = infile.read()
    infile.close()
    return s.count(target)
    
stringCount("example.txt","line")

#####################################################
##### Practice Problem 4.9, Page 113 #################
##################################################### 

# Write function words() that takes one input argument—a file name—and returns the list of actual words (without punctuation symbols !,.:;?) in the file.
# >>> words('example.txt')
# ['The', '3', 'lines', 'in', 'this', 'file', 'end', 'with',
# 'the', 'new', 'line', 'character', 'There', 'is', 'a', 'blank', 'line', 'above', 'this', 'line']

def words(file):
    infile = open(file)
    s = infile.read()
    infile.close()
    table = str.maketrans ("!,.:;?", 6*" ")
    s2=s.translate(table)
    return s2.split()

words ("example.txt")

#####################################################
##### Practice Problem 4.9, Page 114 #################
#####################################################  

# Implement function myGrep() that takes as input two strings, a file name and a target string, and prints every line of the file that contains the target string as a substring.
# >>> myGrep('example.txt', 'line')
# The 3 lines in this file end with the new line character. 
# There is a blank line above this line.

def myGrep(file, target):
    infile= open(file)
    s = infile.readlines()  #since we are checking and printing out after each line. Since readlines puts it in the list, we can iterate and it will be easy to check fro substring
    infile.close()
    for line in s:
        # if target in line # or
        if line.count(target)>0:
            print(line, end = " ")  # without end= " " it prints with a \n space and then next line. To get immediately next line you need to change the print default \n to something else.
    
myGrep("example.txt", "line")





















