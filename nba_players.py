# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:28:13 2024

@author: JC
"""

# Import the libraries
import numpy as np
import pandas as pd
import random
import time
from unidecode import unidecode

# View full Data Frames
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('expand_frame_repr', False)

# Create list of team codes
'''
teams = [
    'atl', 'bos', 'brk', 'cho', 'chi', 'cle', 'dal', 'den', 'det', 'gsw',
    'hou', 'ind', 'lac', 'lal', 'mem', 'mia', 'mil', 'min', 'nop', 'nyk',
    'okc', 'orl', 'phi', 'pho', 'por', 'sac', 'sas', 'tor', 'uta', 'was'
]
'''
# Note: must be in capital letters
teams = ['TOR']

# Create the list of years (seasons)
'''
seasons = ['2014', '2015', '2016', '2017', '2018',
'2019', '2020', '2021', '2022', '2023']
'''
seasons = ['2025']

# Create an empty dataframe to append
nba_players_df = pd.DataFrame()

# Iterate through the seasons
for season in seasons:
    
    # Iterate through the teams
    for team in teams:
        
        # Get the url of the team
        team_url = 'https://www.basketball-reference.com/teams/' + team + \
            '/' + season + '.html'
        print(team_url)
        
        # Get a list of the players
        players = pd.read_html(team_url, header=0, attrs={'id':'roster'})[0]
        print(players)
        
        # Loop through every player
        for player in players.index:
            
            # Grab the current player name
            player_name = players.loc[player, 'Player']
            
            # Grab their first and last name
            # [0] = First Name, [1] = Last Name
            fn_ln = player_name.split()
            
            # Generate their player url
            # https://www.basketball-reference.com/players/d/dickgr01/gamelog/2025/
            # https://www.basketball-reference.com/players/p/poeltja01/gamelog/2025/
            # https://www.basketball-reference.com/players/a/agbajoc01/gamelog/2025/
            player_url = 'https://www.basketball-reference.com/players/' + \
                fn_ln[1][:1].lower() + '/' + fn_ln[1][:5].lower() + \
                fn_ln[0][:2].lower() + '01/gamelog/' + season + '/'
            print(player_url)
            
            # Grab the gamelog table
            plyr_gamelog = pd.read_html(player_url, header=0, attrs={'id':'pgl_basic'})[0]
            
            # Add three columns to the front of plyr_gamelog
            plyr_gamelog.insert(loc=0, column='Season', value=season)
            plyr_gamelog.insert(loc=1, column='Team', value=team)
            plyr_gamelog.insert(loc=2, column='Name', value=fn_ln[0]+' '+fn_ln[1])
            
            # Rename columns
            plyr_gamelog = plyr_gamelog.rename(columns={'Unnamed: 5':'Home', 'Unnamed: 7':'W/L'})
            
            # Replace values in columns 'Home' and 'Opp' of team_df
            plyr_gamelog['Home'] = plyr_gamelog['Home'].apply(lambda x: 0 if x == '@' else 1)

            print(plyr_gamelog)
            
            # Append the current year and team gamelogs to the aggregate dataframe
            nba_players_df = pd.concat([nba_players_df, plyr_gamelog], ignore_index=True)
            
            # Pause program to abide by basketball-reference.com rules
            time.sleep(random.randint(4, 6))

# Export to a CSV File
nba_players_df.to_csv('nba_players_TOR_gamelogs_2025.csv', index=False)