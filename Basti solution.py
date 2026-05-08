5

field = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]   # Leerer string, da Start bei 1

active_player = "X"
run = True

def print_field():
    print(field[1] + "|" + field[2] + "|" + field[3])
    print(field[4] + "|" + field[5] + "|" + field[6])
    print(field[7] + "|" + field[8] + "|" + field[9])

def next_move():
    global run
    while True:
        player_move = input("Bitte das gewünschte Feld eingeben: ")
        if player_move == "q":
            run = False
            return
        # str-input(9 Wert zu int casten
        player_move = int(player_move)
        if player_move >= 1 and player_move <= 9:
            if field[player_move] == "X" or field[player_move] == "0":
                print("Spielfeld ist bereits belegt. Bitte wiederholen ")
            else:
                return player_move
        else:
            print("Die eingegebene Zahl muss zwischen 1 und 9 liegen")


"""Game Loop"""
""" Mit while-true ist eine endlosschleife erzeugt, mit der die einzelnen fuktionen
    des speiel immer aufgerufen werden, bis irgendann false ist"""

def change_player():
    global active_player    # Global sagt, die Variable ist überall zugänglich
    if active_player == "X":
        active_player = "0"
    else:
        active_player = "X"

def check_win():
    #Zeilen prüfen
    if field[1] == field[2] == field[3]:
        return field[1]
    if field[4] == field[5] == field[6]:
        return field[4]
    if field[7] == field[8] == field[9]:
        return field[7]
    # Spalten prüfen
    if field[1] == field[4] == field[7]:
        return field[1]
    if field[2] == field[5] == field[8]:
        return field[2]
    if field[3] == field[6] == field[9]:
        return field[3]
    # Diagonale Prüfen
    if field[1] == field[5] == field[9]:
        return field[1]
    if field[3] == field[5] == field[7]:
        return field[3]


def check_draw():
    if field[1] != "1" and field[2] != "2" and field[3] != "3" and field[4] != "4" and field[5] != "5" and \
        field[6] != "6" and field[7] != "7" and field[8] != "8" and field[9] != "9":
        return True
    


while run:
    print_field()
    player_move = next_move()   # Keine Namens-Kollision, da next_move oben in anderm Bereich
    field[player_move] = active_player
    draw = check_draw()
    winner = check_win()    # Der wert des Spielers der gewonnen hat wird übergeben
    if winner:  # Wenn hier kein leerer String übergeben wird, ist WINNER automatisch TRUE
        print("Spieler " + winner + " hat gewonnen")
        run = False
       
    elif draw:
        print("Das Spiel ist unentschieden!")
        run = False
    change_player()





#print(next_move())


print_field()