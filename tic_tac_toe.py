# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for displaying the board
# by Olivia 8.5.2026

def display_board(grid):
    board = (f"|{grid[1]}|{grid[2]}|{grid[3]}|\n"
             f"|{grid[4]}|{grid[5]}|{grid[6]}|\n"
             f"|{grid[7]}|{grid[8]}|{grid[9]}|")
    print(board)
    


# Function for... (choosing a player?)
def blablabla():
    pass


# ... write as many functions as you need


# Tic-tac-toe game
if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe! \n")

#first grid
first_board= {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}

display_board(first_board)
