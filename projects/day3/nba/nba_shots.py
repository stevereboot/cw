#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""NBA Shot Data Project

Comparing NBA shot data for Kobe, Lebron and Steph from the 
    2015-2016 season.
Data from http://stats.nba.com/

Bloomberg Coding Workshop 2016
"""

import json     # For json parsing

players = ['kobe', 'lebron', 'steph']

# Loop through all players
for player in players:
    # Open file
    file = open(player + '.json')

    # Parse json data into dictionary
    player_data = json.load(file)

    # Extract shot data
    shot_data = player_data['resultSets'][0]

    # Data headers
    headers = shot_data['headers']

    # Shot data
    shots = shot_data['rowSet']

    # Aggregate FG percentages
    shots_fg_made = 0
    shots_fg_att = 0

    for shot in shots:
        # Check if shot is 2 pointer
        if shot[headers.index('SHOT_TYPE')] == '2PT Field Goal':
            # Increment attempts
            shots_fg_att += 1

            # Check if shot was made
            if shot[headers.index('SHOT_MADE_FLAG')]:
                # Increment made
                shots_fg_made += 1

        # Calculate percentage made
        shots_fg_perc = 1.0 * shots_fg_made / shots_fg_att

    # Print ouput
    print 'Player: {:<10} FGM-FGA: {}-{:<10} FG%: {:.2%}'.format(
        player, shots_fg_made, shots_fg_att, shots_fg_perc)