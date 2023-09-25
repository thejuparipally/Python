#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:51:57 2022

@author: theju
"""

# Write and execute the following queries for data from the chinook database in a Python file. 

# When you are done, save and upload your file here:
    
import sqlite3
con = sqlite3.connect("chinook.db")
cur=con.cursor()

# 1) Write a query to display all of the records from the tracks table

sql1 = "SELECT * FROM tracks"
cur.execute(sql1)
results1 = cur.fetchall()

# 2) Write a query to display all of the records from the albums table

sql2 = "SELECT * FROM albums"
cur.execute(sql2)
results2 = cur.fetchall()

# 3) Write a query to display all of the records from the artists table

sql3 = "SELECT * FROM artists"
cur.execute(sql3)
results3 = cur.fetchall()

# 4) Write a query to display Album Name (Title) from the albums table and Song (Name)  
# from the tracks table for each album.

sql4 = '''
SELECT albums.Title, tracks.Name
FROM albums LEFT JOIN tracks
ON albums.albumid =
tracks.albumid
ORDER BY albums.Title
'''
cur.execute(sql4)
results4 = cur.fetchall()

# 5) Write a query to display the Artist Name (Name) from the artists table and the Album Name (Title)
# from the albums table.

sql5 = '''SELECT artists.Name, albums.Title
FROM artists INNER JOIN albums
ON albums.ArtistId =
artists.ArtistId
ORDER BY artists.Name
'''
cur.execute(sql5)
results5 = cur.fetchall()

# 6) Write a query using the chinook database to list all albums, the performing artist, 
# and the number of tracks on the album.

# •Display in 3 columns named:
# •Artist
# •Album
# •TrackCount
# •Output the results of the query to a python list named “FinalResults”

sql6 = '''
SELECT artists.Name AS Artist, albums.Title AS Album, COUNT(Trackid) AS TrackCount
FROM artists
INNER JOIN albums ON albums.ArtistId = artists.ArtistId
INNER JOIN tracks ON albums.albumid = tracks.albumid
GROUP BY albums.Title
'''
cur.execute(sql6)
FinalResults = cur.fetchall()

