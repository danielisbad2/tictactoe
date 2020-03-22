# The board is stored as a list of 9 letters:
# The first 3 form the first row,
# The next 3 are the second row,
# and the final 3 are the last row.
# We start with 9 spaces to represent empty squares.
board = [' ' for i in range(9)]


def print_board(board):
    print('----|---|----')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('----|---|----')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('----|---|----')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('----|---|----')

def print_map():
    print('----|---|----')
    print('| 1 | 2 | 3 |')
    print('----|---|----')
    print('| 4 | 5 | 6 |')
    print('----|---|----')
    print('| 7 | 8 | 9 |')
    print('----|---|----')

def turn(player):
    # Ask the player for the number of the square they want to choose
    choice = int(input(player + ': Where do you want to move? [1-9] '))
    choice -= 1  # Subtract 1 because Python counts from 0

    # Replace the chosen tile with the player's symbol
    board[choice] = player


# Show the players which number corresponds to which square
print_map()

while True:  # We will break out of this loop when the game ends
    print()  # Leave a blank line between turns
    print_board(board)  # Show the current board
    turn('X')  # Allow X to move

    # Do the same thing for O's turn
    print()
    print_board(board)
    turn('O')
