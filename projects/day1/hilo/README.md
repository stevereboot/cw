# Bloomberg Coding Workshop 2016

## HiLo Game Project
A High/Low number guessing game versus the computer

### Project Instructions
In this project, we will build a High/Low number guessing game.  The object of the game is for the user to guess a randomly generated number within a certain number of attempts.  The random number will be within a lower and upper bound that we will tell the user.  After each attempt, the program will tell the user whether their guess was too high, too low or correct.  If the maximum number of attempts is reached, the game will end.

### Files
Filename | Description
---|---
hilo.py | The program

### External Libraries Required
None

### Key Concepts Used
- Imports
- Random Module
- Variables
- Standard I/O
- Casting
- Operator +=
- If-Then-Else
- While Loop
- Break

### Code Walkthrough

#### Imports
Only Python's built-in random library is required to generate the target number.

``` python
import random   # To generate the target number
```

#### Game Settings
We set the 3 main game settings here.

``` python
# Settings
max_tries = 5
lowest = 1
highest = 10
```

#### Printing Instructions For the User
The player needs to guess a number between the lower and upper bounds (inclusive).  They will have limited attempts to guess the right number.

``` python
# Instructions
print 'Welcome to High-Low Guessing Game!'
print 'Guess a number between ' + str(lowest) + ' and ' + str(highest)
print 'You have ' + str(max_tries) + ' attempts'
```

#### Generating a Random Number
We use Python's built-in module random to generate a random number between the lower and upper bound.  Note that random.randrange() does not include the upper bound.  So we use `highest+1` as the upper bound.  Reference [here](https://docs.python.org/2/library/random.html#random.randrange).

``` python
# Generate number to guess
number = random.randrange(lowest, highest+1)    # range excludes upper bound
```

#### Track Number of Attempts
To increase the difficulty factor of our game, we limit the number of attempts users have to guess the random number.  We track the number of attempts in the variable `counter`, which is initialized at 0.

``` python
# Track number of user attempts
counter = 0
```

#### Game loop
In order to keep the game running until the terminal event (either user guesses the number or the limit on attempts is reached), we use an infinite loop.  Inside the loop, we prompt the user to input their guess.  And increment the attempt counter.

``` python
# Game loop, runs until break is reached
while True:
    # Prompt user for guess and store
    guess = int(raw_input('Enter your guess: '))

    # Increment attempt counter
    counter += 1
```

#### Checking the Guess vs Target
We check each guess against the target, and output whether the guess was too high or low back to the user.  If the right number was guessed, we output a congratulatory message with the number of attempts and what the random number was.  Then we break out of the loop and the game ends.

``` python
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
```

#### Monitoring the Attempt Limit
If the user was not able to guess the right answer, we then check if the maximum number of attempts reached.  If so, we output a condolence message with the number of attempts and what the random number was.  Then we break out of the loop and the game ends. Otherwise, the game continues another round.

``` python
    # If number of attempts exceed the limit, the user loses
    if counter == max_tries:
        print 'Sorry! You have guessed more than ' + str(max_tries) + ' times'
        print 'The mystery number was ' + str(number)
        break   # Exit the while loop
```

### Extending this Project
- Add input validation
 - Check to make sure the user actually entered a number between the highest and lowest
 - In the current program, the int casting will throw an error if the user enters a non-numeric character
- Have users input their own game settings at the beginning
- Implement a play-again feature
- Track guesses to prevent duplicates