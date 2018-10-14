# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 11:42:11 2018

@author: clyma
"""
import os
import csv

file_location = os.getcwd()
file = r'\Matchups.csv'
file_location = file_location + file
data = []

with open(file_location) as csvfile:
    contents = csv.DictReader(csvfile)
    for row in contents:
        #print(row)
        if '@' in row['Home']:
            temp = row['Home'].split('@')
            row['Home'] = temp[0].strip()
            row['Away'] = temp[1].strip()
        data.append(row)
        
file = r'\UpdatedMatchups.csv'
file_location2 = os.getcwd() + file
with open(file_location2, 'w') as csvfile:
    fieldnames = ['Week', 'Home', 'Away', 'Day']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in data:
        writer.writerow({fieldnames[0]: i[fieldnames[0]], fieldnames[1]: i[fieldnames[1]], 
                         fieldnames[2]: i[fieldnames[2]], fieldnames[3]: i[fieldnames[3]]})

data = []
with open(file_location2) as csvfile:
    contents = csv.DictReader(csvfile)
    for row in contents:
        data.append(row)
    
        
