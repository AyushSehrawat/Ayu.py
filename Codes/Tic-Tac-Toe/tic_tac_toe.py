import time

import os

import random

# Building  A Tic-Tac-Toe Game

print('Welcome to Tic-Tac-Toe Game!\n---------------------')
time.sleep(1)


def display_board(board):
    os.system('cls')

    print('\n')
    print('  |||||||||||||')
    print('  ____|___|____')
    print('  |' + ' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ' + '|')
    print('------|---|-------')
    print('  |' + ' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ' + '|')
    print('------|---|-------')
    print('  |' + ' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ' + '|')
    print('  ____|___|____')
    print('  |||||||||||||')
    print('\n')
    time.sleep(2)


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):

        marker = input('Player 1: Do you want to be X or O? ').upper()

        if marker == 'X':
            #
            return 'X', 'O'
        #
        return 'O', 'X'


def place_marker(board, marker, posi):
    board[posi] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    return 'Player 1'


def space_check(board, posi):
    return board[posi] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    posi = 0

    while posi not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, posi):
        posi = int(input('Choose your next position: (1-9) '))

    return posi


def wannaplayagain():
    while True:
        wannaplay = input('Would You Like To Play Again,(Y)es or (N)o: ').upper()
        if wannaplay == 'Y':
            return True
        if wannaplay == 'N':
            return False
        print('Wrong Input!')


print("Let's get started!")

while True:

    # Reset the board

    boardy = [' '] * 10

    player1_marker, player2_marker = player_input()

    turn = choose_first()

    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No: ')

    if play_game.lower()[0] == 'y':

        game_on = True

    else:

        game_on = False

    while game_on:

        if turn == 'Player 1':

            # Player1's turn.

            display_board(boardy)

            position = player_choice(boardy)

            place_marker(boardy, player1_marker, position)

            if win_check(boardy, player1_marker):

                display_board(boardy)

                print('Congratulations! You have won the game!')

                game_on = False
            else:

                if full_board_check(boardy):

                    display_board(boardy)

                    print('The game is a draw!')

                    break

                else:

                    turn = 'Player 2'

        else:

            # Player2's turn.

            display_board(boardy)

            position = player_choice(boardy)

            place_marker(boardy, player2_marker, position)

            if win_check(boardy, player2_marker):

                display_board(boardy)

                print('Player 2 has won!')

                game_on = False
            else:
                if full_board_check(boardy):

                    display_board(boardy)

                    print('The game is a draw!')

                    break

                else:
                    turn = 'Player 1'

    if not wannaplayagain():
        break
