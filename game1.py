board = [
['x', 'x', 'x', 'x', 'x'],
['x', 'x', 'x', 'x', 'x'],
['x', 'x', 'RW', 'x', 'x'],
['x', 'x', 'x', 'x', 'x'],
['x', 'x', 'x', 'x', 'x']
]
#LIST[row][col] --> the item you are looking for in a 2D list (GRID).

print(board[2][2])

for row in board:
     print(' '.join(row))
