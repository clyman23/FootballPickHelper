# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 12:24:39 2018

@author: clyman
"""

import requests
from bs4 import BeautifulSoup
import os
import csv


# https://www.pro-football-reference.com/years/2018/games.htm
# Table of the whole schedule for 2018 ^^^

class FootballPool:

    def UpdateTeams(self):
        team_list_address = 'http://www.alphalists.com/list/alphabetical-list-nfl-teams'
        page = requests.get(team_list_address)
        data = page.text
        soup = BeautifulSoup(data, 'lxml')
        team_list_name = soup.find(class_='field-item even')
        team_list_name_items = team_list_name.find('p')
        teams = team_list_name_items.get_text().split('\n\t')
        for i in range(0,len(teams)):
            if 'San Diego' in teams[i]:
                teams[i] = 'Los Angeles Chargers'
            elif 'St. Louis' in teams[i]:
                teams[i] = 'Los Angeles Rams'
        teams.sort()
        return teams
    
    def ChosenTeams(self):
        #Read in file list that store teams that have been picked.
        file_location = os.getcwd()
        filename = r'\ChosenTeams.txt'
        file_location = file_location+filename
        if os.path.isfile(file_location):
            print("File exists")
        else:
            print("File does not exist!")
            return False
        
        with open(file_location, 'r') as file:
            data = file.read()
        data = data.split('\n')
        return data
        
    
    def NewPick(self):
        pick = input("Pick a team: ")
        return pick
    
    def UpdateChosenTeams(self):
        '''Call ChosenTeams() 
        Take user input for new pick
        Add newest input to list
        Save off new chosen teams file
        '''
        new_team = self.NewPick()
        data = self.ChosenTeams()
        file_location = os.getcwd()
        filename = r'\ChosenTeams.txt'
        file_location = file_location+filename
        if os.path.isfile(file_location):
            print("File exists")
        else:
            print("File does not exist!")
            return False
        data.append(new_team)
        with open(file_location, 'w') as file:
            for i in data:
                file.write(i+'\n')
        print("New team = " + new_team)
        print("New team added to file")
    
    
    
    



web_address = 'www.espn.com/nfl/scoreboard/_/year/2018/seasontype/2/week/'
week = '1'



chosen_teams = ['Minnesota Vikings', 'Los Angeles Chargers', 'Seattle Seahawks', 'Jacksonville Jaguars', 'New England Patriots']
valid_teams = []
for i in chosen_teams:
    if i not in teams:
        print("Error! " + i + " not in list")
    else:
        valid_teams.append(i)
        
teams_left = len(teams) - len(valid_teams)
print("You have " + str(teams_left) + " teams left to chose from")


''' Thoughts:
Falcons over Bucs in ATL
Texans over Bills in Houston
Bears over Dolphins in MIA
Rams over Broncos in Denver
Packers over 49ers in GB
'''

