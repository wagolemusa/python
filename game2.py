board = []
for _ in range(5):
     board.append(['0'] * 5)

def print_board(board):
     for row in board:
          print (' '.join(row))
print_board(board)
