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
    print('| 0 | 1 | 2 |')
    print('----|---|----')
    print('| 3 | 4 | 5 |')
    print('----|---|----')
    print('| 6 | 7 | 8 |')
    print('----|---|----')

def print_winner(board, winner):
    print()
    print_board(board)  # Display the final board
    print()
    print(winner, 'has won!')  # Show which player won
    print()

def turn(player):
    while True:
        # Ask the player for the number of the square they want to choose
        str_choice = input(player + ': Where do you want to move? [0-8] ')

        try:
            # Attempt to convert the input to an integer
            choice = int(str_choice)
        except ValueError:
            # They did not input a valid number
            print('Please select a number!')
        else:
            # A valid number was entered
            if choice >= 0 and choice <= 8:
                # Check whether this tile is taken
                if board[choice] == ' ':
                    # This selection is allowed!
                    # Replace the chosen tile with the player's symbol
                    board[choice] = player
                    return  # End the running of this function and loop
                else:
                    # This tile has already been claimed
                    print('Someone has already moved there!')
            else:
                # Number is not between 1 and 9
                print('You must select a number between 0 and 8!')

def is_winner(bo, pl):
    # Check if player `pl` has won, with board being shortened to `bo`
    return (
        (bo[0] == pl and bo[1] == pl and bo[2] == pl) or  # Across the top
        (bo[3] == pl and bo[4] == pl and bo[5] == pl) or  # Across the middle
        (bo[6] == pl and bo[7] == pl and bo[8] == pl) or  # Across the bottom
        (bo[0] == pl and bo[3] == pl and bo[6] == pl) or  # Down the left side
        (bo[1] == pl and bo[4] == pl and bo[7] == pl) or  # Down the middle
        (bo[2] == pl and bo[5] == pl and bo[8] == pl) or  # Down the right side
        (bo[0] == pl and bo[4] == pl and bo[8] == pl) or  # Diagonal
        (bo[2] == pl and bo[4] == pl and bo[6] == pl)     # Diagonal
    )

def get_winner(board):
    # Check if either player has won
    if is_winner(board, 'X'):
        return 'X'
    elif is_winner(board, 'O'):
        return 'O'
    elif all([x != ' ' for x in board]):
        # The board is full, but nobody has won (a draw)
        return 'Nobody'
    else:
        return None


# The board is stored as a list of 9 letters:
# The first 3 form the first row,
# The next 3 are the second row,
# and the final 3 are the last row.
# We start with 9 spaces to represent empty squares.
board = [' ' for i in range(9)]

# Show the players which number corresponds to which square
print_map()

while True:  # We will break out of this loop when the game ends
    print()  # Leave a blank line between turns
    print_board(board)  # Show the current board
    turn('X')  # Allow X to move

    # Check if someone has won
    winner = get_winner(board)
    if winner is not None:
        print_winner(board, winner)

    # Do the same thing for O's turn
    print()
    print_board(board)
    turn('O')

    # Check if someone has won
    winner = get_winner(board)
    if winner is not None:
        print_winner(board, winner)
