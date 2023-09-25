#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 18:02:28 2022

@author: theju
"""

import sqlite3
con = sqlite3.connect("chinook.db")
cur=con.cursor()

sql1 = "SELECT name, milliseconds, bytes, albumid FROM tracks WHERE albumid = 1"
cur.execute(sql1)
results1 = cur.fetchall()

sql2 = "SELECT name, milliseconds, bytes, albumid FROM tracks WHERE milliseconds > 250000"
cur.execute(sql2)
results2 = cur.fetchall()

sql3 = "SELECT name, milliseconds, bytes, albumid FROM tracks WHERE albumid = 1 AND milliseconds > 250000"
cur.execute(sql3)
results3 = cur.fetchall()

sql4 = '''SELECT name, albumid, composer
FROM tracks
WHERE composer LIKE '%Smith'
ORDER BY albumid'''
cur.execute(sql4)
results4 = cur.fetchall()

sql5 = '''SELECT name, albumid, composer
FROM tracks
WHERE composer LIKE '%Smith%'
ORDER BY albumid'''
cur.execute(sql5)
results5 = cur.fetchall()

sql6 = '''SELECT trackid, name
FROM tracks
WHERE name LIKE 'Wild%'
'''
cur.execute(sql6)
results6 = cur.fetchall()

sql7 = '''SELECT trackid, name
FROM tracks
WHERE name LIKE '%Wild%'
'''
cur.execute(sql7)
results7 = cur.fetchall()

################# IN OPERATOR ##########################

sql8 = '''SELECT TrackId, Name,
MediaTypeId
FROM Tracks
WHERE MediaTypeId = 1 OR
MediaTypeId = 2
ORDER BY Name ASC     
'''

# ORDER BY Name ASC (do not need this anyway because it is that as default)

cur.execute(sql8)
results8 = cur.fetchall()

#or/ can also be written as

sql9 = ''' SELECT TrackId, Name,
Mediatypeid
FROM Tracks
WHERE MediaTypeId IN (1, 2)
ORDER BY Name ASC 
'''
cur.execute(sql9)
results9 = cur.fetchall()

################# INNER JOIN ##########################

sql10 = '''SELECT trackid, name, title
FROM tracks INNER JOIN albums
ON albums.albumid =
tracks.albumid
'''

#or (being more specific on which values to call from where)

sql10 = '''SELECT tracks.trackid, tracks.name, albums.title
FROM tracks INNER JOIN albums
ON albums.albumid =
tracks.albumid
'''

#or (alias notation)

sql10 = '''SELECT t.trackid, t.name, a.title
FROM tracks t INNER JOIN albums a
ON albums.albumid =
tracks.albumid
'''
# sql10 = '''SELECT t.trackid, t.name, a.title
# FROM tracks AS t INNER JOIN albums AS a
# ON albums.albumid =
# tracks.albumid
# '''

cur.execute(sql10)
results10 = cur.fetchall()

################# LEFT JOIN ##########################

sql11 = '''SELECT artists.ArtistId, AlbumId
FROM artists LEFT JOIN albums
ON albums.ArtistId =
artists.ArtistId
ORDER BY AlbumId
'''
cur.execute(sql11)
results11 = cur.fetchall()

sql11 = '''SELECT artists.ArtistId, Name, Title, AlbumId
FROM artists LEFT JOIN albums
ON albums.ArtistId =
artists.ArtistId
ORDER BY AlbumId
'''
cur.execute(sql11)
results11 = cur.fetchall()

################# INNER JOIN ##########################

sql12 = '''SELECT artists.ArtistId, AlbumId
FROM artists INNER JOIN albums
ON albums.ArtistId =
artists.ArtistId
ORDER BY AlbumId
'''
cur.execute(sql12)
results12 = cur.fetchall()

################# SELF JOIN ##########################

sql13 = '''
SELECT
m.firstname || ' ' || m.lastname AS 'Manager',
e.firstname || ' ' || e.lastname AS 'Direct report'
FROM employees e INNER JOIN employees m
ON m.employeeid = e.reportsto
ORDER BY manager
'''
cur.execute(sql13)
results13 = cur.fetchall()

################# UNION ##########################


sql14 = ''' 
SELECT FirstName, LastName,
'Employee' AS Type
FROM employees
UNION
SELECT FirstName, LastName,
'Customer' AS Type
FROM customers
'''

cur.execute(sql14)
results14 = cur.fetchall()

# Union removes common fields and returns all. But UNION ALL returns the duplicate columns as well
# For it to work it should have same number of columns/fields and same field names that are common

################# SUB QUERY ##########################

# basically use an output in a new query to create new table

sql15 = '''
SELECT customerid, firstname,
lastname
FROM customers
WHERE supportrepid IN (
SELECT employeeid
FROM employees
WHERE country = 'Canada')
'''
cur.execute(sql15)
results15 = cur.fetchall()

sql16 = '''
SELECT AVG(album.size)
FROM (
SELECT SUM(bytes) AS SIZE
FROM tracks
GROUP BY albumid ) AS album
'''

cur.execute(sql16)
results16 = cur.fetchall()

################# IN CLASS ASSIGNMENT ##########################


# Write a query to list all albums, the performing artist, and the number
# of tracks on the album.
# • Display in 3 columns named:
# • Artist
# • Album
# • TrackCount
# • Output the results of the query to a python list named “results”

sql17 = " SELECT artists.Name, albums. Title,  "


