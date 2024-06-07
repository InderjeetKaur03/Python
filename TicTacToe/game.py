'''
Display the game board
'''
def display_game_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])
    
'''
Asl player to choose the marker type of x or o
'''    
def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker = input('Player 1 : Choose X or O : ').upper()
    
    if marker=='X':
        return ('X','O')
    else:
         return ('O','X')  


'''
Update the cosen location in board for a player
'''
def place_marker(board, marker, position):
    board[position] = marker

'''
Check for winning condition
'''    
def win_check(board, mark):
   return ((board[1] == mark and board[2]== mark and board[3] == mark) or 
    (board[4] == mark and board[5]== mark and board[6] == mark) or 
    (board[7] == mark and board[8]== mark and board[9] == mark) or 
    (board[1] == mark and board[4]== mark and board[7] == mark) or 
    (board[2] == mark and board[5]== mark and board[8] == mark) or 
    (board[3] == mark and board[6]== mark and board[9] == mark) or 
    (board[1] == mark and board[5]== mark and board[9] == mark) or 
    (board[7] == mark and board[5]== mark and board[3] == mark))

'''
Choose a player Randomly
'''
import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 1:
        return 'Player 1'
    else:
        return 'Player 2'

'''
Check if board location if space is available
'''
def check_space(board, position):
    return board[position] == ' '

'''
Check if board is full
'''
def check_board_full(board):
    for i in range(1,10):
        if check_space(board,i):
            return False
    return True

'''
Ask player for next position, first check if it is available else chose another
'''
def player_choice(board):
    position =0
    while position not in [1,2,3,4,5,6,7,8,9] or not check_space(board,position):
        position = int(input('Choose a position : (1-9) : ') )
    return position

'''
Ask if palyer want to play again
'''
def play_again():
    choice = input('Want to play another game (Y/N): ').lower()
    return choice =='y'

##############################################################################################
'''
Logic to play the game and call the functions above
'''

# While loop to keep running the game
print('Welcome to TIC TAC TOE')

while True:
    #Play the game
    ## Set the board, who goes first, choose markers, X,O
    test_board = [' ']*10
    player1_marker, player2_marker = player_input()
    print('Player 1 will use : ' + player1_marker + ', Player 2 will use : ' + player2_marker)
    turn = choose_first()
    print(turn + ' goes first')

    play_game = input('Ready to play (y/n): ').lower()

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    ## Playing the game
    while game_on:
        if turn == 'Player 1':
            print('Player 1 turn, '+player1_marker+ ' will be filled')
            display_game_board(test_board)
            #choose the position
            position = player_choice(test_board)
            #place the marker on the position
            place_marker(test_board,player1_marker, position)
            #check if they won
            if win_check(test_board, player1_marker):
                display_game_board(test_board)
                print('Player 1 has won!!')
                game_on = False
            # no win, then next player's turn
            else:
                if check_board_full(test_board):
                    display_game_board(test_board)
                    print('No one won, its a tie')
                    game_on = False
                else:
                    turn = 'Player 2'
        else: 
        ### Player 2 turn 
            print('Player 2 turn'+player2_marker+ 'will be filled')       
            display_game_board(test_board)
            #choose the position
            position = player_choice(test_board)
            #place the marker on the position
            place_marker(test_board,player2_marker, position)
            #check if they won
            if win_check(test_board, player2_marker):
                display_game_board(test_board)
                print('Player 2 has won!!')
                game_on = False
            # no win, check for tie, then next player's turn
            else:
                if check_board_full(test_board):
                    display_game_board(test_board)
                    print('No one won, its a tie')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not play_again():
        break
# Break the while loop on reply no to play_again function