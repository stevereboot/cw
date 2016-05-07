#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Citibike Data Project

Analyze Citibike ride data.
Data from https://www.citibikenyc.com/system-data

Bloomberg Coding Workshop 2016
"""

import csv  # For csv parsing

files = ['citibike-tripdata']

# Loop through files
for file in files:
    # Open file
    f = open(file + '.csv')

    # Parse csv data
    csv_data = csv.reader(f)

    # Store csv data as a list
    ride_data = list(csv_data)

    # First row are the headers
    headers = ride_data[0]

    # Ride data
    rides = ride_data[1:]

    # Aggregate ride data
    avg_time = 0
    min_time = None
    max_time = 0
    ride_ct = 0

    for ride in rides:
        # Calculate trip length
        ride_time = float(ride[headers.index('tripduration')])

        # Check if time is shortest or longest so far
        if not min_time: min_time = ride_time

        if ride_time < min_time:
            # Set new shortest time
            min_time = ride_time
        elif ride_time > max_time:
            # Set new longest time
            max_time = ride_time

        # Calculate average time
        ride_ct += 1
        avg_time = avg_time * (ride_ct-1)/ride_ct + ride_time / ride_ct

    # Print ouput
    print 'File: {:25} Rides: {:<10,} Avg Time: {:<0.2f}m   Min-Max Time: {:,.2f}m-{:,.2f}m'.format(
        file, ride_ct, avg_time/60, min_time/60, max_time/60)