#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Hot-Cold Game Project
A Hot/Cold number guessing game versus the computer

Bloomberg Coding Workshop 2016
"""

import random   # To generate the target number

# Instructions
print 'Welcome to Hot-Cold Guessing Game!'
print 'Guess a number between 1 and 100'

# Generate number to guess
randomNumber = random.randrange(1, 101)    # Will return a number 1-100

# Track number of user attempts
tries = 0

# Initialize variable to hold user guess
guessedNumber = -1

# Game loop, runs until the user guesses the right number
while randomNumber != guessedNumber:
    # Prompt user for guess and store
    guessedNumber = int(raw_input('Enter your guess: '))
    
    # Increment attempt counter
    tries = tries + 1

    # Check if guess is within the bounds of the game (1-100)
    if guessedNumber < 1  or guessedNumber > 100 :
        print 'The number should be between 1 and 100. Try again!'
    # If so, check how close the guess is to the target and output a hint
    elif abs(randomNumber - guessedNumber) >= 50:
        print 'Arctic Cold'
    elif abs(randomNumber - guessedNumber) >= 40:
        print 'Ice Cold'
    elif abs(randomNumber - guessedNumber) >= 30:
        print 'Cold'
    elif abs(randomNumber - guessedNumber) >= 20:
        print 'Luke Warm'
    elif abs(randomNumber - guessedNumber) >= 10:
        print 'Warm'
    elif abs(randomNumber - guessedNumber) >= 5:
        print 'Hot!'
    elif abs(randomNumber - guessedNumber) >= 2:
        print 'Hot Hot Hot!!!'        
    elif abs(randomNumber - guessedNumber) >= 1:
        print 'Nuclear Hot!!!!!!!!!!'

# If loop exits, it means the user has guessed the random number
print 'BINGO!!'
print randomNumber, 'is the correct number. Good work!'
print 'It took you', tries, 'tries.'