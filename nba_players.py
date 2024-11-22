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

# Create list of team codes
'''
teams = [
    'atl', 'bos', 'brk', 'cho', 'chi', 'cle', 'dal', 'den', 'det', 'gsw',
    'hou', 'ind', 'lac', 'lal', 'mem', 'mia', 'mil', 'min', 'nop', 'nyk',
    'okc', 'orl', 'phi', 'pho', 'por', 'sac', 'sas', 'tor', 'uta', 'was'
]
'''
teams = ['tor']

# Create the list of years (seasons)
'''
seasons = ['2014', '2015', '2016', '2017', '2018',
'2019', '2020', '2021', '2022', '2023']
'''
seasons = ['2024']

# Create an empty dataframe to append
nba_df = pd.DataFrame()

# Iterate through the seasons
for season in seasons:
    
    # Iterate through the teams
    for team in teams:
        
        # Get the url of the team
        url = 'https://www.basketball-reference.com/teams/' + team + '/' + season + '.html'
        print(url)
        
        # Get a list of the players
        players = pd.read_html(url, header=1, attrs={id})

