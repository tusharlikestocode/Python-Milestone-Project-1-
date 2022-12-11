import random
def choose_first():
    if random.randint(0,1)==0:
        return 'Player1'
    else:
        return 'Player2'
def display_board(board):


    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
def place_maker(board,marker,position):
    board[position]=marker

# place_maker(test_board,'+',1)
# display_board(test_board)
# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board,position):
    return board[position]==' '
# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False

    return True
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('choose your next position:(1-9)'))
    return position
def replay():
    return input('do you want to play again?enter yes or no: ').lower().startswith('y')
print("Welcome to Tic Tac Toe!")
while True:
    theBoard = [' ']*10
    player1_marker, player2_maker=player_input()
    turn = choose_first()
    print(turn + " will goes first")
    play_game = input("are you ready to play? enter yes or no.")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_maker(theBoard,player1_marker,position)
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('congratulations!player1 wins')
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("the game is draw!")
                    break
                else:
                    turn='Player2'
        else:
            display_board(theBoard)
            position=player_choice(theBoard)
            place_maker(theBoard,player2_maker,position)
            if(win_check(theBoard,player2_maker)):
                display_board(theBoard)
                print('congratulations!player2 wins')
                game_on = False

            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("the game is draw!")
                    break
                else:
                    turn = 'Player1'

    if not replay():
        break
