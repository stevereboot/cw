#!/usr/bin/env python

"""tictactoe.py: A tic-tac-toe game."""

# Prints each character in the board array
def printBoard( board ) :
    print()
    for line in board:
        for char in line:
            print( char, end="")
        print()
    print()

# Gets input, adds move to the board and returns ' ' or the winner
def handleUser( userChar, board ):
    print( "Player " + userChar + ", input coordinates:" )
    move = input()
    coords = move.split( " " )
    i = int( coords[0] )
    j = int( coords[1] )
    board[ i ][ j ] = userChar
    printBoard( board )
    
########### EXTRA-CREDIT ############
    return getWinner( board ) 
    

def main():
    # Define data objects
    board = [ [".", ".", "."],
              [".", ".", "."],
              [".", ".", "."] ]
    winner = " "
    
    # Begin program
    print( "Welcome to tic-tac-toe." )
    print( "Each player will input coordinates." )
    print( "E.g \"0 0\" for the top left, \"1 2\" for top right" )
    printBoard( board )
    print()
    print( "Player X, you go first." )
    
    # Game loop
    while( True ):
        winner = handleUser( 'X', board )
        if winner != " ":
            break;
            
        winner = handleUser( 'O', board )
        if winner != " ":
            break;
       
    print( "Congratulations " + winner + "!" )

        
########### EXTRA-CREDIT ############
# Returns ' ' or 'X' or 'O'
def getWinner( board ) :
    for char in [ "X", "Y" ]:
        # Check rows
        winner = board[0][0] == board[0][1] == board[0][2] == char
        if winner :
            return char
        winner = board[1][0] == board[1][1] == board[1][2] == char 
        if winner :
            return char
        winner = board[2][0] == board[2][1] == board[2][2] == char 
        if winner : 
            return char
            
        # Check columns
        winner = board[0][0] == board[1][0] == board[2][0] == char 
        if winner == char :
            return char
        winner = board[0][1] == board[1][1] == board[2][1] == char 
        if winner :
            return char
        winner = board[0][2] == board[1][2] == board[2][2] == char 
        if winner : 
            return char
            
        # Check diagonals
        winner = board[0][0] == board[1][1] == board[2][2] == char 
        if winner :
            return char
        winner = board[0][2] == board[1][1] == board[2][0] == char 
        if winner :
            return char
        
        return " "

main()