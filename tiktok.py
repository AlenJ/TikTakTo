possible_Moves =  [" "] * 9
player_one_moves = [10] *5
player_Two_moves = [11] *5
winning_combinations = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 5, 7], [3, 6, 9], [4, 5, 6], [7, 8, 9]]



def cls():
    print("\n" * 100)

def get_Player_Char():
    x = input()
    if x == "X" or x == "x":
        return "X"  
    elif x == "o" or x == "O":
        return "O"
    
def get_player_move(player):
        
    print("Player "+ player + " please select a number from 1 to 9:")
    move = input()
    return int(move)

def check_if_valid_move(a, b):
    if any(i in a for i in b):
        print("Not valid move, please try again")
    else:
        return True
    return False
    

def print_canvas():
    vertical  = "   |   |   "
    horizontal = "-----------"
    print(vertical)
    print(" " + possible_Moves[0] + " | " + possible_Moves[1] + " | " + possible_Moves[2])
    print(vertical)
    print(horizontal)
    print(vertical)
    print(" " + possible_Moves[3] + " | " + possible_Moves[4] + " | " + possible_Moves[5])
    print(vertical)
    print(horizontal)
    print(vertical)
    print(" " + possible_Moves[6] + " | " + possible_Moves[7] + " | " + possible_Moves[8])
    print(vertical)
    
# Main
print("Player one please Select X or O:")

player_One_ch = get_Player_Char() 
if player_One_ch == "X":
    player_Two_ch = "O"
else:
    player_Two_ch = "X"

print_canvas()

turn = 0;
while turn < 5:
    
    
    playerOneMove = get_player_move("one")
    player_one_moves[turn] = playerOneMove
    possible_Moves[ playerOneMove-1 ] = player_One_ch
    cls()
    player_one_moves.sort()
    print_canvas()
    
    if all(i in player_one_moves for i in winning_combinations[0]):
        print("win!")
        break
            
    if all(i in player_one_moves for i in winning_combinations[1]):
        print("win!")
        break
            
    if all(i in player_one_moves for i in winning_combinations[2]):
        print("win!")
        break
            
    if all(i in player_one_moves for i in winning_combinations[3]):
        print("win!")
        break
            
    if all(i in player_one_moves for i in winning_combinations[4]):
        print("win!")
        break
            
    if all(i in player_one_moves for i in winning_combinations[5]):
        print("win!")
        break
            
    if all(i in player_one_moves for i in winning_combinations[6]):
        print("win!")
        break
            
    if all(i in player_one_moves for i in winning_combinations[7]):
        print("win!")
        break
        

   
    valido = False
    
    while valido == False:
        playerTwoMove = get_player_move("two")
        player_Two_moves[turn] = playerTwoMove
        valido = check_if_valid_move(player_Two_moves, player_one_moves)
    possible_Moves[playerTwoMove-1] = player_Two_ch
    cls()
    player_Two_moves.sort()
    print_canvas()
    
    if all(i in player_Two_moves for i in winning_combinations[0]):
        print("win!")
        break
            
    if all(i in player_Two_moves for i in winning_combinations[1]):
        print("win!")
        break
            
    if all(i in player_Two_moves for i in winning_combinations[2]):
        print("win!")
        break
            
    if all(i in player_Two_moves for i in winning_combinations[3]):
        print("win!")
        break
            
    if all(i in player_Two_moves for i in winning_combinations[4]):
        print("win!")
        break
            
    if all(i in player_Two_moves for i in winning_combinations[5]):
        print("win!")
        break
            
    if all(i in player_Two_moves for i in winning_combinations[6]):
        print("win!")
        break
            
    if all(i in player_Two_moves for i in winning_combinations[7]):
        print("win!")
        break
    
  
    
    turn = turn + 1
