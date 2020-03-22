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


# The board is stored as a string of 9 letters. This would look something
# like "XXXOOOXXX". The first 3 form the first row, the next 3 are the second
# row and the final 3 are the last row.
board = ' ' * 9

# Show the players which number corresponds to which square
print_map()
