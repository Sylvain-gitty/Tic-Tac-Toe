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
 # define turn_number variable before the function
def playersmove(turn_number):
        #ASking for the user input and adding the input to the grid
        # Check if the value is X or O , if yes, ask for new input with print "somebody already played here"
        # Check if the value is outside of range, and ask for new input , print (its outside the board)
        # Assign X for the fist plyer and O for the second player

    print("Select a position:")
    position = input() 
    # print(turn_number) # turn_number has to be a counter in the loop
    if str.isdigit(position) and int(position) in (board):        
        #else: #update board
        if turn_number % 2 == 0: sign = "X" 
        else: sign = "O"
        board[int(position)] = sign
        display_board(board)
    else:
        print("Position is not available or is not a digit:")
    return    



# Function for... (choosing a player?)


# ... write as many functions as you need
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
    #elif turn_number > 9:
        # check if every cell is filled
    for position in grid:
        if grid[position] not in ["X" , "O"]:
            return False
    else:
    # If we reach here, it's a draw
         print("It's a draw!")
    return True

#creates first board
board= {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}

turn_number = 1
display_board(board)
playersmove(turn_number)

while checkdraw(board) == False and checkwin(board) == False:
        turn_number += 1
        playersmove(turn_number)
        
        
## WHAT DOESNT WORK AND NEEDS HELP:
# DRAW UNDER DEVELOPMENT
# IF INPUT ALREADY INPUTTED SHOULD GIVES A MESSAGE AND ASK FOR NEW INPUT 
# PRINT ITS A WIN TWICE INSTEAD OF ONE'
