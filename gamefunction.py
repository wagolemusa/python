from random import randint

board = []

for x in range(0, 5):
     board.append(["0"] * 5)
def print_board(board):
     for row in board:
          print (' '.join(row))

print_board(board)

def random_row(board):
     return randint(0, len(board) - 1)

def random_col(board):
     return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print (ship_row) 
print (ship_col)

quess_row = int(input('Guess Row: '))
quess_col = int(input('Guess Col: '))



if quess_row == ship_row and quess_col == ship_col:
     print("Congratulation! you sank my battleship!")
else:
     print("You failed to Guess")
