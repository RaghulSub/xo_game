import os


board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

co = [False]*9         # it tracks position of X and O

co_player_O = [False]*9

co_player_X = [False]*9


def print_board():
    
    print("\t\tTIC TAC TOE\n\n")
    print('\t\t\t\t','0 |','1 |','2')
    print("\t\t\t\t-----------")
    print('\t\t\t\t','3 |','4 |','5')
    print("\t\t\t\t-----------")
    print('\t\t\t\t','6 |','7 |','8')
    
    print(' ',board[0],'|',board[1],'|',board[2])
    print(" -----------")
    print(' ',board[3],'|',board[4],'|',board[5])
    print(" -----------")
    print(' ',board[6],'|',board[7],'|',board[8])
    
def condition_O():       #this is used to check that user O is occupied the position and also to check user O is win or not
    
    is_win = False
    if co_player_O[0] and co_player_O[1] and co_player_O[2]:
        is_win = True
    elif co_player_O[3] and co_player_O[4] and co_player_O[5]:
        is_win = True
    elif co_player_O[6] and co_player_O[7] and co_player_O[8]:
        is_win = True
    elif co_player_O[0] and co_player_O[3] and co_player_O[6]:
        is_win = True
    elif co_player_O[1] and co_player_O[4] and co_player_O[7]:
        is_win = True
    elif co_player_O[2] and co_player_O[5] and co_player_O[8]:
        is_win = True
    elif co_player_O[0] and co_player_O[4] and co_player_O[8]:
        is_win = True
    elif co_player_O[2] and co_player_O[4] and co_player_O[6]:
        is_win = True
        
    if is_win:
        print_board()
        print("\n!!!  Player \'O\' won the game  !!!")
        return True
    return False
        
    
   
def condition_X():       #this is used to check that user O is occupied the position and also to check user O is win or not
    
    is_win = False
    if co_player_X[0] and co_player_X[1] and co_player_X[2]:
        is_win = True
    elif co_player_X[3] and co_player_X[4] and co_player_X[5]:
        is_win = True
    elif co_player_X[6] and co_player_X[7] and co_player_X[8]:
        is_win = True
    elif co_player_X[0] and co_player_X[3] and co_player_X[6]:
        is_win = True
    elif co_player_X[1] and co_player_X[4] and co_player_X[7]:
        is_win = True
    elif co_player_X[2] and co_player_X[5] and co_player_X[8]:
        is_win = True
    elif co_player_X[0] and co_player_X[4] and co_player_X[8]:
        is_win = True
    elif co_player_X[2] and co_player_X[4] and co_player_X[6]:
        is_win = True
        
    if is_win:
        print_board()
        print("\n!!!  Player \'X\' won the game  !!!")
        return True
    return False 
    

    
    
    
    
def input_board_player_O():   #this is used to take input from user1
    x = int(input("Enter the position of ' O ' : "))
    co[x] = True
    co_player_O[x] = True
    board[x] = 'O'
    os.system('cls')
def input_board_player_X():     #this is used to take input from user2
    x = int(input("Enter the position of ' X  ' : "))
    co[x] = True
    co_player_X[x] = True
    board[x] = 'X'
    os.system('cls')
    
def is_end():
    _end = False
    if False in co:
        _end = True
    return _end
    
    
while(True):
    
    print_board()
    input_board_player_O()
    if condition_O():
        break
    
    if not is_end():                           
        print_board()
        print("\n!!!  Its a Draw  !!!")
        break
    
    print_board()
    input_board_player_X()
    if condition_X():
        break               # This condition is to check whether all the box are filled or not
    

    
 
