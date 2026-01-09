import random

# Step 1: Create a 10x10 board filled with '.'
board = [['.' for _ in range(10)] for _ in range(10)]

# Step 2: Function to draw the board
def drawBoard(board):
    print("  ", end="")
    for column in range(10):
        print(column, end=" ")
    print()
    for row in range(10):
        print(row, end=" ")
        for col in board[row]:
            print(col, end=" ")
        print()

# Step 3: Randomly place 5 ships ('S')
NUM_SHIPS = 5
ships_placed = 0
while ships_placed < NUM_SHIPS:
    row = random.randint(0, 9)
    col = random.randint(0, 9)
    if board[row][col] == '.':
        board[row][col] = 'S'
        ships_placed += 1

# Step 4: Function to check hit or miss
def checkHitOrMiss(board, row, col):
    if board[row][col] == 'S':
        board[row][col] = 'X'
        return "HIT"
    elif board[row][col] == 'X':
        return "HIT"
    else:
        board[row][col] = 'O'
        return "MISS"

# Step 5: Function to check if game is over
def isGameOver(board):
    for row in board:
        if 'S' in row:
            return False
    return True

# Step 6: Main game loop
print("Welcome to Battleship!")
while True:
    drawBoard(board)
    try:
        col = int(input("Enter column (0-9): "))
        if col < 0 or col > 9:
            print("Invalid column! Try again.")
            continue
        row = int(input("Enter row (0-9): "))
        if row < 0 or row > 9:
            print("Invalid row! Try again.")
            continue
    except ValueError:
        print("Please enter a number between 0 and 9.")
        continue

    result = checkHitOrMiss(board, row, col)
    print(result)

    if isGameOver(board):
        drawBoard(board)
        print("GAME OVER! All ships sunk!")
        break
