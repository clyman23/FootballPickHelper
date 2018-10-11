# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 12:24:39 2018

@author: clyman
"""

import requests
from bs4 import BeautifulSoup

# https://www.pro-football-reference.com/years/2018/games.htm
# Table of the whole schedule for 2018 ^^^

team_list_address = 'http://www.alphalists.com/list/alphabetical-list-nfl-teams'
page = requests.get(team_list_address)
data = page.text
soup = BeautifulSoup(data, 'lxml')

team_list_name = soup.find(class_='field-item even')
team_list_name_items = team_list_name.find('p')
teams = team_list_name_items.get_text().split('\n\t')

web_address = 'www.espn.com/nfl/scoreboard/_/year/2018/seasontype/2/week/'
week = '1'

for i in range(0,len(teams)):
    if 'San Diego' in teams[i]:
        teams[i] = 'Los Angeles Chargers'
    elif 'St. Louis' in teams[i]:
        teams[i] = 'Los Angeles Rams'

chosen_teams = ['Minnesota Vikings', 'Los Angeles Chargers', 'Seattle Seahawks', 'Jacksonville Jaguars', 'New England Patriots']
valid_teams = []
for i in chosen_teams:
    if i not in teams:
        print("Error! " + i + " not in list")
    else:
        valid_teams.append(i)
        
teams_left = len(teams) - len(valid_teams)
print("You have " + str(teams_left) + " teams left to chose from")


