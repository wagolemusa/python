from random import randint

board = []

for x in range(0, 5):
     board.append(["0"] * 5)
def print_board(board):
     for row in board:
          print " ".join(row)

def random_row(board):
     return randint(0, len(board) - 1)

def random_col(board):
     return randint(0, len(board) - 1)

random_row(board)
random_col(board)
                 
