#Python 3 Console Tic Tac Toe 2-player Game

#TODO 
#Player Registration
#Game field drawing
#Gameplay

def PrintRow(row):
    for i in row:
        print(i, end = '', sep = ' ')
    print('')
    

print('Welcome to Tic Tac Toe! \n')

player1 = input('Enter first player name: ')
#player2 = input('Enter second player name: ')

row0 = [' ', ' ', '7', ' ', '8', ' ', '9', ' ']
row1 = ['7', '|', ' ', '|', ' ', '|', ' ', '|', '9']
row2 = ['4', '|', ' ', '|', ' ', '|', ' ', '|', '6']
row3 = ['1', '|', ' ', '|', ' ', '|', ' ', '|', '3']
row4 = [' ', ' ', '1', ' ', '2', ' ', '3', ' ']

PrintRow(row0)
PrintRow(row1)
PrintRow(row2)
PrintRow(row3)
PrintRow(row4)

print('Use numpad keys to make a move.\n')
print(player1, end='')
player1_move = input(':')

