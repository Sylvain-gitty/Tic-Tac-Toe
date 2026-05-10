# Function for:
# 1. creating a 3x3 dictionary for the game board,
# 2. displaying the updated board
# by Olivia-sajjad 10.5.2026

def display_board(grid):

    # Improved game board with closed boxes
    board = (
        "\n"
        "+---+---+---+\n"
        f"| {grid[1]} | {grid[2]} | {grid[3]} |\n"
        "+---+---+---+\n"
        f"| {grid[4]} | {grid[5]} | {grid[6]} |\n"
        "+---+---+---+\n"
        f"| {grid[7]} | {grid[8]} | {grid[9]} |\n"
        "+---+---+---+"
    )

    print(board)


# 3. Define a function to handle player input
# and update the game board accordingly.

def playersmove(turn_number):

    # Player identification
    if turn_number % 2 == 0:
        sign = "O"
        print("\nPlayer 2 (O) turn")
    else:
        sign = "X"
        print("\nPlayer 1 (X) turn")

    print("Select a position (1-9) or q to quit:")

    position = input()

    # Added quit option
    if position.lower() == "q":
        print("Game exited.")
        exit()

    # print(turn_number) # turn_number has to be a counter in the loop

    if str.isdigit(position) and int(position) in (board):

        # Assign X for first player and O for second player
        board[int(position)] = sign
        display_board(board)

    else:
        print("Position is not available or is not a digit:")

    return


# WIN CONDITIONS:
# Check within the grid if values of
# row/columns/diagonals are the same
# and not empty, then we have a winner.

def checkwin(grid):

    if grid[1] == grid[2] == grid[3] in ["X", "O"]:
        print("It's a win!")
        return True

    elif grid[4] == grid[5] == grid[6] in ["X", "O"]:
        print("It's a win!")
        return True

    elif grid[7] == grid[8] == grid[9] in ["X", "O"]:
        print("It's a win!")
        return True

    elif grid[1] == grid[4] == grid[7] in ["X", "O"]:
        print("It's a win!")
        return True

    elif grid[2] == grid[5] == grid[8] in ["X", "O"]:
        print("It's a win!")
        return True

    elif grid[3] == grid[6] == grid[9] in ["X", "O"]:
        print("It's a win!")
        return True

    elif grid[1] == grid[5] == grid[9] in ["X", "O"]:
        print("It's a win!")
        return True

    elif grid[3] == grid[5] == grid[7] in ["X", "O"]:
        print("It's a win!")
        return True

    else:
        return False


# DRAW CONDITIONS:
# Check if all cells are filled
# and no winner, then we have a draw.

def checkdraw(grid):

    # Check if there is a winner
    if checkwin(grid):
        return False

    # Check if every cell is filled
    for position in grid:

        if grid[position] not in ["X", "O"]:
            return False

    else:
        # If we reach here, it's a draw
        print("It's a draw!")

    return True


# Creates first board
board = {
    1: '1', 2: '2', 3: '3',
    4: '4', 5: '5',
    6: '6', 7: '7',
    8: '8', 9: '9'
}

turn_number = 1

print("=== TIC TAC TOE ===")

# Display starting board
display_board(board)

playersmove(turn_number)

while checkdraw(board) == False and checkwin(board) == False:

    turn_number += 1
    playersmove(turn_number)