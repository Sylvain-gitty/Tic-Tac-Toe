# Common Tic Tac Toe Implementation
# def 

#Pseudocode Time:
#1. Create a 3x3 dictionary for the game board.
def create_dic():
    grid = {1: " ", 2: " ", 3: " ",  # WE NEED TO ADD THE VALUES FOR VISUAL EFFECT FOR THE USER
            4: " ", 5: " ", 6: " ",
            7: " ", 8: " ", 9: " "}
    return grid
#2. Define a function to display the game board.
def display_board(grid):
    print_board() # We want each cell to be surrounded by a border, so we will use "|" and "-" to create the grid lines.

#3. Define a function to handle player input and update the game board accordingly.
def playersmove()
        #ASking for the user input and adding the input to the grid
        # Check if the value is X or O , if yes, ask for new input with print "somebody already played here"
        # Check if the value is outside of range, and ask for new input , print (its outside the board)
        # Assign X for the fist plyer and O for the second player

# WIN CONDITIONS:
 # Check within the grid if values of row/columns/diegonales are the same and not empty, then we have a winner.
 #break the loop, print "winner etc"

 def checkwin()=
    if(grid[1] == grid[2] == grid[3]):
    print("It's a win!") 
    return True 
    elif(grid[4] == grid[5] == grid[6]):
    
    Checkif(grid[7] == grid[8] == grid[9] != "
            #ETC FOR EVERY POSITIONS
    return True
    if True:
        print("We have a winner! Do you want to play again?"[y,n]) # If no input  for 1 minute, close the game
        break
        

 # DRAW CONDITIONS:
    # Check if all cells are filled and no winner, then we have a draw.
def checkdraw(grid):
    # check if there is a winner
    if checkwin(grid):
        return False
    # check if every cell is filled
    for position in grid:
        if grid[position] not in ["X" OR "0"]:
            return False
    # If we reach here, it's a draw
    print("It's a draw!")
    return True
