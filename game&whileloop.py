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

#print (ship_row) 
#print (ship_col)

#using while loop
guesses = 0
while guesses < 4:
     musa_row = int(raw_input('Guess Row: '))
     musa_col = int(raw_input('Guess Col: '))

     #This checks if you guessed correctly
     if musa_row == ship_row and musa_col == ship_col:
          print("Congratulation! you sank my battleship!")
          break #guesses = 4

     #This checks if you guessed within the 5x5 grid.    
     elif musa_row not in  range(5) or  musa_col not in range(5):
          print("Oops, that's not even the ocean")

     #this tells you, you missed and makes that spot as X.
     elif board[musa_row][musa_col] == 'x':
          print("You guessed that one already.")
               
     else:
          print("You missed my battleship!")
          board[musa_row][musa_col] = 'x'
          print_board(board)
          guesses = guesses + 1
          if guesses == 4:
               print("Game is over! You have run out of Turns!")
                      
