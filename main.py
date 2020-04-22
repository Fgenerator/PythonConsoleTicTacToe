#Python 3 Console Tic Tac Toe 2-player Game

#TODO 
#Player Registration
#Game field drawing
#Gameplay

def print_field():
    print_row(row0)
    print_row(row1)
    print_row(row2)
    print_row(row3)  
    print_row(row4)

def print_row(row):
    for i in row:
        print(i, end = '', sep = ' ')
    print('')
    
def make_a_move(move, sign):
    row, cell = input_to_cell[move]
    row[cell] = sign 

def check_a_move(move):
    row, cell = input_to_cell[move]
    if row[cell] == ' ':
        return True
    else:
        print('Cell is not empty!')
        return False

def clear_field():
    
    global row0 
    global row1 
    global row2 
    global row3 
    global row4 

    row0 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    row1 = [' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ']
    row2 = [' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ']
    row3 = [' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ']
    row4 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def start():
    
    print_field()
    count = 0
    check = False
    
    print('Use numpad keys (1-9) to make a move.\n')
    
    for i in range(9):
            if count % 2 == 0:
                
                while check == False:
                    print(player1, end='')
                    player_move = input(':')
                    check = check_a_move(player_move)
               
                make_a_move(player_move, sign1)
                print_field()
                player_move = 0
                check = False
                count += 1
            else:
                
                while check == False:
                    print(player2, end='')
                    player_move = input(':')
                    check = check_a_move(player_move)
                
                make_a_move(player_move, sign2)
                print_field()
                player_move = 0
                check = False
                count += 1
    f = input('Press Enter to start a New Game')
    if f == '':
        clear_field()
        start()
    else:
        exit()        

print('Welcome to Tic Tac Toe! \n')

player1 = 'player1'
sign1 = 'x'

player2 = 'player2'
sign2 = 'o'

#player1 = input('Enter first player name: ')
#sign1 = input('Choose your sign - x or o: ')

#player2 = input('Enter second player name: ')
#sign2 = input('Choose your sign - x or o: ')

row0 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
row1 = [' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ']
row2 = [' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ']
row3 = [' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ']
row4 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

input_to_cell = {
    '1': (row3, 2),
    '2': (row3, 4),
    '3': (row3, 6),
    '4': (row2, 2),
    '5': (row2, 4),
    '6': (row2, 6),
    '7': (row1, 2),
    '8': (row1, 4),
    '9': (row1, 6),   
}

start()



