# Function for:
# 1. creating a 3x3 dictionary for the game board, 
# 2. displaying the updated board 
# by Olivia 8.5.2026

def display_board(grid):
    board = (f"|{grid[1]}|{grid[2]}|{grid[3]}|\n"
             f"|{grid[4]}|{grid[5]}|{grid[6]}|\n"
             f"|{grid[7]}|{grid[8]}|{grid[9]}|")
    print(board)
    

#3. Define a function to handle player input and update the game board accordingly.
def playersmove():
        #ASking for the user input and adding the input to the grid
        # Check if the value is X or O , if yes, ask for new input with print "somebody already played here"
        # Check if the value is outside of range, and ask for new input , print (its outside the board)
        # Assign X for the fist plyer and O for the second player

    print("Select a position:")
    position = input()
    if str.isdigit(position) and int(position) in (board):
        #if not position in {"X", "O"}:
        #   print ("Please enter X or O:")
        #else: #update board
        board[int(position)] = "X" # who is the first player?
        display_board(board)

    else:
        print("Position is not available or is not a digit:")
    return        

    

# Function for... (choosing a player?)


# ... write as many functions as you need


# Tic-tac-toe game
#if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe! \n")

#creates first board
board= {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}

display_board(board)

playersmove()