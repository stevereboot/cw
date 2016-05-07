#!/usr/bin/env python
import sys


# Set up file reader
if len( sys.argv ) != 2:
    print "Error: requires exactly one command line argument to specify input file."
    exit( 1 )

f = open( sys.argv[1], 'r' )

# Set up variables for storage
linesRead = 0

maxPop = 0
maxPopCountyName = ''

maxMenToWomen = 0.0
maxMToFCounty = ''

# Loop through the data, aggregating in the variables
for line in f:
    linesRead = linesRead + 1
    fields = line.split(',')
    ageGrp = int( fields[2] )
    # Only care about the 'All' age group for now
    if ( ageGrp == 0 ):

        stateName = fields[0]
        cityName = fields[1]
        pop = int( fields[3] )
        malePop = int( fields[4] )
        femalePop = int( fields[5] )

        if pop > maxPop:
            maxPop = pop
            maxPopCountyName = cityName

        menToWomen = malePop / femalePop
        if menToWomen > maxMenToWomen:
            maxMenToWomen = menToWomen
            maxMToFCounty = cityName

# Print out results
print "Number of lines read: %d" % linesRead
print "Max population: %s %d" % ( maxPopCountyName, maxPop )
print "Max Men To Women Ratio: %s %d" % ( maxMToFCounty, maxMenToWomen )

# Successful exit
exit(0)
