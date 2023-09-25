#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 18:03:47 2022

@author: theju
"""


#####################################################
######################### SQL #######################
#####################################################

import sqlite3
con = sqlite3.connect("web_crawler.db")
cur=con.cursor()

sql1 = "SELECT * FROM Keywords"
cur.execute(sql1)
results1 = cur.fetchall()

#to select UNIQUE URL from Keywords

sql2 = "SELECT DISTINCT URL FROM Keywords"
cur.execute(sql1)
results2 = cur.fetchall()

# to show URL by descending order (by default it shows by ascending is DESC is not written)

sql3 = "SELECT DISTINCT URL FROM Keywords ORDER BY URL DESC"
cur.execute(sql1)
results3 = cur.fetchall()

# to show URL, Freq by descending order of Freq

sql4 = "SELECT DISTINCT URL, Freq FROM Keywords ORDER BY URL DESC"
cur.execute(sql1)
results4 = cur.fetchall()

#####################################################
###### Practice Problem 12.1, Page 405 #############
#####################################################

# Write an SQL query that returns:
# (a) The URL of every page that has a link to web page four.html
# (b) The URL of every page that has an incoming link from page four.html
# (c) The URL and word for every word that appears exactly three times in the web page associated with the URL
# (d) The URL, word, and frequency for every word that appears between three and five times, inclusive, in the web page associated with the URL

sql5 = "SELECT Url FROM Hyperlinks WHERE Link = 'four.html'"
cur.execute(sql5)
results5 = cur.fetchall()

sql6 = "SELECT Link FROM Hyperlinks WHERE Url = 'four.html'"
cur.execute(sql6)
results6 = cur.fetchall()

sql7 = "SELECT Url, Word FROM Keywords WHERE Freq = 3"
cur.execute(sql7)
results7 = cur.fetchall()

sql8 = "SELECT * FROM Keywords WHERE Freq BETWEEN 3 AND 5"
cur.execute(sql8)
results8 = cur.fetchall()

# sql8 = '''
# SELECT *
# FROM Keywords 
# WHERE Freq > 3 AND Freq < 5
# '''
# cur.execute(sql4)
# results8 = cur.fetchall()

#Count function 

# sql9= " SELECT Url, COUNT(*) FROM Hyperlinks GROUP BY Url "
# cur.execute(sql9)
# results9= cur.fetchall()

#####################################################
###### Practice Problem 12.2, Page 407 #############
#####################################################

# For each question, write an SQL query that answers it:
# (a) How many words,including duplicates,does page two.html contain? 
# (b) How many distinct words does page two.html contain?
# (c) How many words, including duplicates, does each web page have?
# (d) How many incoming links does each web page have?
# The result tables for questions (c) and (d) should include the URLs of the web pages.

sql9 = "SELECT Url, SUM(Freq) FROM Keywords WHERE Url = 'two.html'"
cur.execute(sql9)
results9 = cur.fetchall()

sql10 = "SELECT Count(Word) FROM Keywords WHERE Url = 'two.html'"     # "SELECT Count(*) FROM Keywords WHERE Url = 'two.html'"
cur.execute(sql10)
results10 = cur.fetchall()

sql11 = "SELECT Url, SUM(Freq) FROM Keywords GROUP BY Url"
cur.execute(sql11)
results11 = cur.fetchall()

sql12 = "SELECT Link, Count(Url) FROM Hyperlinks GROUP BY Link"
cur.execute(sql12)
results12 = cur.fetchall()

cur.close()    # always close the cursor at the end of the program 
con.close()    # always close the cursor at the end of the program 

