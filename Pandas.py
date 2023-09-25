#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 18:29:04 2022

@author: theju
"""

# Pandas Data Structures
# There are two main data structures in Pandas:
# 1) DataFrame – a two-dimensional array of values with both a row and a column index
# 2) Series – a one-dimensional array of values with an index

# Loading data into Pandas data structures

import pandas as pd

###############################################################################
# Typing Data into a Pandas Dataframe and a Series #
###############################################################################

# Data Frame

df1 = pd.DataFrame(data = [
['NJ', 'Towaco', 'Square'],
['CA', 'San Francisco', 'Oval'],
['TX', 'Austin', 'Triangle'],
['MD', 'Baltimore', 'Square'],
['OH', 'Columbus', 'Hexagon'],
['IL', 'Chicago', 'Circle']
],
columns = ['State', 'City', 'Shape'])

# Series

ser1 = pd.Series(data=['NJ', 'CA', 'TX', 'MD', 'OH', 'IL'], name= 'States')

dictAQI = {
'color': ['Green', 'Yellow', 'Orange', 'Red', 'Purple', 'Maroon'],
'concern': ['Good', 'Moderate', 'Unhealthy for Sensitive Groups',
'Unhealthy', 'Very Unhealthy', 'Hazardous'],
'low': [0, 51, 101, 151, 201, 301],
'high':[50, 100, 150, 200, 300, 999]
}

dfAQI = pd.DataFrame(dictAQI)
print(dfAQI)

###############################################################################
# Importing Data from a CSV file into a Pandas Dataframe #
###############################################################################

df2 = pd.read_csv("/Users/theju/Desktop/USD/Business Analytics Fund./ECTs.csv")

###############################################################################
# Importing Data from SQL into a Pandas Dataframe #
###############################################################################

import sqlite3
con = sqlite3.connect('/Users/theju/Desktop/USD/Business Analytics Fund./chinook.db')

sql1 = """SELECT Artist, Title, COUNT(Track) as TrackCount FROM (
SELECT artists.Name as Artist, albums.Title, tracks.Name as Track, genres.Name as Genre
FROM artists INNER JOIN albums ON artists.ArtistId = albums.ArtistId
LEFT JOIN tracks ON albums.AlbumId = tracks.AlbumId
LEFT JOIN genres ON tracks.GenreId = genres.GenreId
ORDER BY Artist)
GROUP BY Artist, Title;"""
sql2 = 'SELECT * FROM customers WHERE country ="USA"'

df3 = pd.read_sql_query(sql1, con)
df4 = pd.read_sql_query(sql2, con)
con.close()

###############################################################################
# Importing Data from an Excel file into a Pandas Dataframe #
###############################################################################

df5 = pd.read_excel("/Users/theju/Desktop/USD/Business Analytics Fund./States.xlsx", sheet_name = "Sheet1")

# Exploratory Data Analysis with Pandas

###############################################################################
# Summarizing Values in a Pandas Dataframe #
###############################################################################

ser1.head()    #returns first 5 rows default
ser1.tail()    # returns last 5 rows
len(ser1)      # returns length
ser1.count()   # returns count
ser1.dtypes    # returns data types of each column: Here it is O- object (Same as text)
ser1.info()    # displays types and counts of each data column
ser1.describe()  # gives summary (like descriptive statistics)

df2.head(9)    #returns first 9 rows default
df2.tail()
df2.dtypes
df2_summary = df2.describe()     #This is similar to summary(df2) in R. Gives only descriptive statistics on numerical columns
df2['Series_title_2'].describe() #Calling descriptive statistics on categorical column by mentioning the column name
df2['Series_title_2'].value_counts()
df2.isnull()      # returns binary value 0/1 T/F if there is a null value for each column
df2.isnull().sum()      # counts the number of null values for each column
df2['UNITS'].value_counts() #counts the number of unique values in that column
df2['Period']  # called slicing. Just calling one column values
ser3 = pd.Series (data = df2['Period'])  #can save it as new df to use it further
df1.iloc[0, 2]    # returns value at row 0 and column 2
df2.iloc[12,:]    # returns values everything after column 12
df2.iloc[:,1]     # returns values till column 1 

# We can use it in a loop to:

a=0
for i in range(len(ser3)):
    a += ser3.iloc[i]

### Sorting

df2 = df2.sort_values(["Data_value"])  # To sort in ascending order. Default
df2 = df2.sort_values(["Data_value"], ascending = False) # to sort in descending order

### Filtering

df2_negative = df2[df2["Data_value"] < 0]   #returns negative data values 
df4_California = df4[df4["State"] == 'CA']  # returns data values that have state CA

### Pivot Table
###https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html

df_PT = pd.pivot_table(df2, values = ['Data_value'], index = ['UNITS', 'Series_title_2'], dropna=(True)) #by default by doing pivot table it will sum
df_groupby = df2.groupby(['UNITS', 'Series_title_2']).mean()['Data_value']  # gives mean
df_groupby = df2.groupby(['UNITS', 'Series_title_2']).count()['Data_value'] #gives count


### JOIN

###https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

df_join1 = pd.merge(df1, df5, how = 'right', on='State')   # joins two tables df1, df5, how tells which join and on which primary/foregin key
df_join2 = pd.merge(df4, df5, how = 'inner', on = 'State')

#Output files

df1.to_csv("/Users/theju/Desktop/USD/Business Analytics Fund./Example1.csv", sep = "|", index=False) #save output as csv with delimiter 
df2.to_excel('/Users/theju/Desktop/USD/Business Analytics Fund./foo.xlsx', sheet_name = "Sheet_Foo")  # save output as excel




