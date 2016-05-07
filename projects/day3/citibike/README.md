# Bloomberg Coding Workshop 2016

## Citibike Data Project
Analyze Citibike ride data

Data from https://www.citibikenyc.com/system-data

Weather data from https://www.ncdc.noaa.gov/cdo-web/datasets

### Project Instructions
In this project, we will analyze Citibike ride data from the first half of March 2016.  Ride data includes the duration of the trip, start and ending stations and some demographic data for subscribers.  Parse the data file and output the total number of rides, the average, min and max times.

### Files
The csv file inside data.7z should be extracted and put into the same directory as citibike.py

Filename | Description
---|---
citibike.py | Script to load, parse and analyze Citibike csv data
data.7z | CSV data files compressed
  -- citibike-tripdata.csv | Citibike ride data for Mar 1-15 2016  (annual subscribers only)
  -- weather.csv | OPTIONAL: For extending the project.  Not used in project

### External Libraries Required
None

### Key Concepts Used
- Imports
- Variables
- For Loop
- Opening Files
- Csv parsing
- Dictionary
- If-Then-Else
- List
- Casting
- Operator +=
- String Formatting

### Code Walkthrough

#### Imports
Only Python's built-in csv library is required to parse the ride data
``` python
import csv  # For csv parsing
```

#### Variables
We will store file names in a list which we will iterate through next.  Although there is only one in this example, more can be added as an extension to this project.

``` python
files = ['citibike-tripdata']
```

#### Loop Through the Ride Data
Inside the loop, we open the the ride data csv file and parse it into a readere object called `csv_data`.  We will then convert this into a list. Then extract the headers in the first row and the ride data in the rest of the rows.

``` python
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

```

#### Aggregating Data
Create some variables to hold the aggregated data we are looking for.

``` python
    # Aggregate ride data
    avg_time = 0
    min_time = None
    max_time = 0
    ride_ct = 0
```

Create a new loop to aggregate the ride lengths.  Shortest and longest rides are stored and the average ride time is calculated.

``` python
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
```

#### Ouput
Output is printed using python's native string formatting.  Reference [here](https://docs.python.org/2/library/stdtypes.html#str.format).

``` python
    # Print ouput
    print 'File: {:25} Rides: {:<10,} Avg Time: {:<0.2f}m   Min-Max Time: {:,.2f}m-{:,.2f}m'.format(
        file, ride_ct, avg_time/60, min_time/60, max_time/60)
```

### Extending this Project
- Calculate more stats, ex: which routes are common, peak times, weekdays vs weekends, etc
- Clean up outliers, ex: longest trip is 47,097 minutes!
- Incorporate weather data into analysis
- Download more time periods from [here](https://s3.amazonaws.com/tripdata/index.html)