#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HiLo Game Project

A High/Low guessing game versus the computer

Bloomberg Coding Workshop 2016
"""

import random   # To generate the target number

# Settings
max_tries = 5
lowest = 1
highest = 10

# Instructions
print 'Welcome to High-Low Guessing Game!'
print 'Guess a number between ' + str(lowest) + ' and ' + str(highest)
print 'You have ' + str(max_tries) + ' attempts'

# Generate number to guess
number = random.randrange(lowest, highest+1)    # range excludes upper bound

# Track number of user attempts
counter = 0

# Game loop, runs until break is reached
while True:
    # Prompt user for guess and store
    guess = int(raw_input('Enter your guess: '))

    # Increment attempt counter
    counter += 1

    # Check if guess is higher or lower than the target number
    if guess > number:
        print 'Your guess is too high'
    elif guess < number:
        print 'Your guess is too low'
    else:
        # Otherwise, the guess and the target match and the user wins
        print 'Congrats! You guessed it after ' + str(counter)+ ' attempt(s)'
        print 'The mystery number was ' + str(number)
        break   # Exit the while loop

    # If number of attempts exceed the limit, the user loses
    if counter == max_tries:
        print 'Sorry! You have guessed more than ' + str(max_tries) + ' times'
        print 'The mystery number was ' + str(number)
        break   # Exit the while loop