# Create a Tic Tac Toe game
# Here are the requirements:
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

import string

# Function to display the grid


def display_board(input_lst):
    # print('  ' + ' | ' + ' ' + ' | ' + ' ')
    # print('  ' + '|' + '  ' + ' | ' + ' ')
    print(' ' + input_lst[1] + ' | ' + input_lst[2] + ' | ' + input_lst[3])
    print('---|---|---')
    # print('  ' + '| ' + ' ' + ' | ' + ' ')
    print(' ' + input_lst[4] + ' | ' + input_lst[5] + ' | ' + input_lst[6])
    # print('  ' + ' | ' + ' ' + ' | ' + ' ')
    print('---|---|---')
    # print('  ' + '| ' + ' ' + ' | ' + ' ')
    print(' ' + input_lst[7] + ' | ' + input_lst[8] + ' | ' + input_lst[9] + '\n')
    # print('  ' + ' |' + '  ' + ' | ' + ' ')


# Function to validate player input choice
def check_player_choice(player_choice, player_number):
    if player_number == 1:
        if player_choice not in string.ascii_uppercase or player_choice == '':
            print('Incorrect choice')
            p1_input_choice()
    elif player_choice not in string.ascii_uppercase or player_choice == p1_choice or player_choice == '':
        print('Incorrect choice')
        p2_input_choice()
    else:
        print('Choice selection complete\n')


# Function to get input choice from Player 1
def p1_input_choice():
    global p1_choice
    p1_choice = input('Player 1, please choose any letter between A to Z:  ').upper()
    check_player_choice(p1_choice, 1)


# Function to get input choice from Player 2
def p2_input_choice():
    global p2_choice
    p2_choice = input('Player 2, please choose any letter between A to Z different from the choice of player 1:  ').upper()
    check_player_choice(p2_choice, 2)


# Function to validate player block choice
def check_block_choice(player_bloc_choice):
    if player_bloc_choice not in range(1, 10):
        print('Selected block out of range, please select an integer between 1 and 9')
        check_block = False
    elif input_lst[player_bloc_choice] != ' ':
        print('This block is already filled')
        check_block = False
    else:
        check_block = True

    return check_block


# Function to let player 1 pick a block to place his input choice
def p1_block_choice():
    p1_bloc_choice = int(input('Player 1, please select the block number between 1 and 9: '))
    check_output = check_block_choice(p1_bloc_choice)
    if check_output:
        input_lst[p1_bloc_choice] = p1_choice
    else:
        p1_block_choice()


# Function to let player 12pick a block to place his input choice
def p2_block_choice():
    p2_bloc_choice = int(input('Player 2, please select the block number between 1 and 9: '))
    check_output = check_block_choice(p2_bloc_choice)
    if check_output:
        input_lst[p2_bloc_choice] = p2_choice
    else:
        p2_block_choice()


# Function to check if the game has a winner
def check_winner():
    check1 = False
    check2 = False
    check3 = False
    check4 = False
    global completion_check
    global input_lst

    for j in range(1, 8):
        if (input_lst[j] != ' ' and input_lst[j+1] != ' ' and input_lst[j+2] != ' ') and (input_lst[j] == input_lst[j+1] == input_lst[j+2]):
            check1 = True
        else:
            continue

        j += 3

    for k in range(1, 4):
        if (input_lst[k] != ' ' and input_lst[k+3] != ' ' and input_lst[k+6] != ' ') and (input_lst[k] == input_lst[k+3] == input_lst[k+6]):
            check2 = True
        else:
            continue

        k += 1

    if (input_lst[1] != ' ' and input_lst[5] != ' ' and input_lst[9] != ' ') and (input_lst[1] == input_lst[5] == input_lst[9]):
        check3 = True

    if (input_lst[3] != ' ' and input_lst[5] != ' ' and input_lst[7] != ' ') and (input_lst[3] == input_lst[5] == input_lst[7]):
        check4 = True

    if check1 or check2 or check3 or check4:
        completion_check = True


# Code execution Starts here
# Just to add a new line at the start of the output
print('\n')

# Get user inputs
p1_input_choice()
p2_input_choice()

# Store the inputs in a dictionary
input_choice_list = {"p1": p1_choice, "p2": p2_choice}

print(input_choice_list)

# Display all the block numbers
input_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

print('\nBelow are the block numbers: ')
display_board(input_lst)

print('\nAlternate between each other by selecting the blocks from 1 to 9 to form a sequence')

input_lst = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# display_board(input_lst)
global completion_check
completion_check = False

for i in range(1, 10):
    display_board(input_lst)

    if i % 2 == 0:
        p2_block_choice()
    else:
        p1_block_choice()

    # Check for a winner after the current move
    check_winner()

    if completion_check:
        if i % 2 == 0:
            winner = 'Player 2'
        else:
            winner = 'Player 1'

        print('\n********   GAME COMPLETE, ' + winner + ' won the game   ********')
        break

'''for i in range(1, 10):
    display_board(input_lst)
    print(input_lst)
    # while completion_check == 0:
    if i % 2 == 0:
        p2_block_choice = int(input('Player 2, please select the block number:  '))
        input_lst[p2_block_choice] = p2_choice
        # check_result()
    else:
        p1_block_choice = int(input('Player 1, please select the block number between 1 and 9:  '))
        input_lst[p1_block_choice] = p1_choice'''


display_board(input_lst)
