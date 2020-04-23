#Python 3 Console Tic Tac Toe 2-player Game

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
    if move != '1' and move != '2' and move != '3' and move != '4' and move != '5' and move != '6' and move != '7' and move != '8' and move != '9':
        print('Wrong move! Use 1-9 keys.')
        return False
    else:
        row, cell = input_to_cell[move]
        if row[cell] == ' ':
            return True
        else:
            print('Cell is not empty!')
            return False

def check_row(row, sign):
    if row[2] == row[4] == row[6] == sign:
        row[2] = '-'
        row[4] = '-'
        row[6] = '-'
        print_field()

        if sign == sign1:
            print(player1, 'won!')
        elif sign == sign2:
            print(player2, 'won!')
        return True
    else:
        return False

def check_rows(row1, row2, row3, sign1, sign2):
    if check_row(row1, sign1) == True:
        return True
    elif check_row(row1, sign2) == True:
        return True
    elif check_row(row2, sign1) == True:
        return True
    elif check_row(row2, sign2) == True:
        return True
    elif check_row(row3, sign1) == True:
        return True
    elif check_row(row3, sign2) == True:
        return True
    else:
        return False

def check_column(column, sign):
    if row1[column * 2] == row2[column * 2] == row3[column * 2] == sign:
        row1[column * 2] = '|'
        row2[column * 2] = '|'
        row3[column * 2] = '|'
        print_field()

        if sign == sign1:
            print(player1, 'won!')
        elif sign == sign2:
            print(player2, 'won!')
        return True
    else:
        return False

def check_columns():
    if check_column(1, sign1) == True:
        return True
    elif check_column(1, sign2) == True:
        return True
    elif check_column(2, sign1) == True:
            return True
    elif check_column(2, sign2) == True:
            return True
    elif check_column(3, sign1) == True:
            return True
    elif check_column(3, sign2) == True:
            return True
    else:
        return False
    
def check_diagonals(sign):
    if row1[2] == row2[4] == row3[6] == sign:
        row1[2] = '\\'
        row2[4] = '\\'
        row3[6] = '\\'
        print_field()

        if sign == sign1:
            print(player1, 'won!')
        elif sign == sign2:
            print(player2, 'won!')
        return True
    if row1[6] == row2[4] == row3[2] == sign:
        row1[6] = '/'
        row2[4] = '/'
        row3[2] = '/'
        print_field()

        if sign == sign1:
            print(player1, 'won!')
        elif sign == sign2:
            print(player2, 'won!')
        return True
    else:
        return False


def check_win_line(row1, row2, row3, sign1, sign2):
    if check_rows(row1, row2, row3, sign1, sign2) == True:
        return True
    elif check_columns() == True:
        return True
    elif check_diagonals(sign1) == True:
        return True
    elif check_diagonals(sign2) == True:
        return True
    else:
        return False

def start():
    
    print_field()
    count = 0
    check = False
    
    print('Use numpad keys (1-9) to make a move.\n')
    
    while check_win_line(row1, row2, row3, sign1, sign2) != True:

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
        
          

print('Welcome to Tic Tac Toe! \n')

player1 = input('Enter first player name: ')
sign1 = input('Choose your sign - x or o: ')[0]

player2 = input('Enter second player name: ')
sign2 = input('Choose your sign - x or o: ')[0]

while True:
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
    f = input('Start a New game? (y/n)')
    if f == 'y':
        print('')
    else:
        exit()  