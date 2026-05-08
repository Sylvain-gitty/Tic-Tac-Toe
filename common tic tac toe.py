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

# WIN CONDITIONS:
 # Check within the grid if values of row/columns/diegonales are the same and not empty, then we have a winner.
 #break the loop, print "winner etc"

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
    # Check if all cells are filled and no winner, then we have a draw.
def checkdraw(grid):
    # check if there is a winner
    if checkwin(grid):
        return False
    # check if every cell is filled
    for position in grid:
        if grid[position] not in ["X" OR "O"]:
            return False
    # If we reach here, it's a draw
    print("It's a draw!")
    return True

# PALY AGIAN
def play_again():
    choice = input("Do you want to play again? (y/n): ").lower().strip()
    if choice == "y":
        return True
    else:
        print("Game Over. Thanks for playing!")
        sys.exit()