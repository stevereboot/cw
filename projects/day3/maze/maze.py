#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Maze Runner Project

Implement controls to navigate through a maze.
Get more mazes at http://www.delorie.com/game-room/mazes/genmaze.cgi

Bloomberg Coding Workshop 2016
"""

# Define function to print maze to screen
def print_maze(maze):
    """Prints the maze object to the screen

    The maze object is a 2-dimensional list.
    """
    for line in maze:
        print ' '.join(line)

# Open maze file
maze_file = open('maze3.txt')

# List to hold the maze
maze = []

# Player position (and start position)
pos_x = -1
pos_y = -1

# Exit position
exit_x = -1
exit_y = -1

# Start with the first line
line_ctr = 0

# Loop through each line of file
for line in maze_file:
    # Temporary list to hold each line
    maze_line = []

    # Start with the first character
    char_ctr = 0

    # Loop through each character in the line
    for character in line:
        # Check if we are at the end of the line
        if character != '\n':
            # Check for map start and end positions
            if character == 'S':
                # Map start position
                pos_x = char_ctr
                pos_y = line_ctr
                # Place the player indicator, 'O', at the start position
                character = 'O'
            elif character == 'E':
                # Map end position
                exit_x = char_ctr
                exit_y = line_ctr

            # Add character to the line list
            maze_line.append(character)

        # Evaluate next character
        char_ctr += 1

    # Add finished line to the maze list
    maze.append(maze_line)

    # Evaluate next line
    line_ctr += 1

# Game loop, runs until break is reached
while True:
    # Print maze to the screen
    print_maze(maze)
    
    # If the player position are at the exit coordinates, game ends
    if (pos_y == exit_y and pos_x == exit_x):
        print 'Congratulations, you made it out of the maze!'
        break
    
    # Prompt user to make a move
    userInput = raw_input('Please enter a move (w/a/s/d): ')

    # Erase old player indicator
    maze[pos_y][pos_x] = ' '

    # User tries to go up
    if (userInput == 'w' and pos_y != 0 and maze[pos_y - 1][pos_x] != 'X'):
        pos_y = pos_y - 1

    # User tries to go left
    elif (userInput == 'a' and pos_x != 0 and maze[pos_y][pos_x - 1] != 'X'):
        pos_x = pos_x - 1
        
    # User tries to go down
    elif (userInput == 's' and pos_y != len(maze) - 1 and maze[pos_y + 1][pos_x] != 'X'):
        pos_y = pos_y + 1
        
    # User tries to go right
    elif (userInput == 'd' and pos_x != len(maze[pos_y]) - 1 and maze[pos_y][pos_x + 1] != 'X'):
        pos_x = pos_x + 1
    
    # Invalid input
    else:
        print('Invalid move!')

    # Add new player indicator
    maze[pos_y][pos_x] = 'O'