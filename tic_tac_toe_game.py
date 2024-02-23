import os

# DATA

# Board
board_list = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# 'How to play' display board
how_to_play_board_list = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Nested list of winning line combinations
winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8],
                        [3, 6, 9], [1, 5, 9], [3, 5, 7]]

# Setting which player's turn it is
current_player = 1

# Setting the winner decided boolean
winner_decided = False

# Setting the game turned on boolean so the user can play again

game_on = True

# Counting games played and how many times each player has won

games_played = 0
player_one_wins = 0
player_two_wins = 0

# FUNCTIONS

def display_board(board_list):    # Display the current board
    print("\n {7} | {8} | {9}\n-----------\n {4} | {5} | {6}\n-----------\n {1} |\
 {2} | {3}\n".format(*board_list))

def player_turn_display():    # Printing whose turn it is
    if current_player == 1:
        print('Player one: Your turn\n')
    else:
        print('Player two: Your turn\n')
        
def player_turn(board_list, current_player):    # Taking a turn
    
    player_chosen_a_square = False
    
    if current_player == 1:    # Defining player marker symbols
        player_marker = 'X'
    else:
        player_marker = 'O'

    while not player_chosen_a_square:    # Player choosing a square
        player_square_choice = input('Choose a square: ')

        if not player_square_choice.isdigit() or not 1 <= int(player_square_choice) <= 9:
            print('\nInvalid input\n')
        elif board_list[int(player_square_choice)] != ' ':
            print('\nSquare already taken\n')
        else:
            board_list[int(player_square_choice)] = player_marker
            player_chosen_a_square = True
  
    return board_list

def print_winner_message(winner):    # Prints a message stating the winner
    print(f'Winner! Player {winner}!\n')
    global winner_decided, games_played, player_one_wins, player_two_wins
    if winner == 'One':
        player_one_wins += 1
    else:
        player_two_wins += 1
    games_played += 1
    winner_decided = True

def check_for_winner(board_list):    # Checking if there's a winner
    for i in winning_combinations:
        if board_list[(i[0])] == board_list[(i[1])] == board_list[(i[2])] and (board_list[(i[0])] == 'X' or board_list[(i[0])] == 'O'):
            if board_list[(i[0])] == 'X':
                print_winner_message('One')
            else:
                print_winner_message('Two')
        else:
            pass

def check_for_stalemate(board_list):     # Checking if all 9 squares are filled
    global games_played, winner_decided
    if ' ' not in board_list:
        print('Game over! Draw!\n')
        games_played += 1
        winner_decided = True

def change_players_turn(current_player):
    if current_player == 1:    # Changing whose turn it is
        return 2
    else:
        return 1
    
def play_again_check():    # Asking the user if they want to play again

    while True:

        user_choice = input('Play again? Y or N? ').upper()

        if user_choice == 'Y':
            return True
        elif user_choice == 'N':
            return False
        else:
            print('\nInvalid input.\n')

def display_game_results(games_played, player_one_wins, player_two_wins):

    # Display the total number of wins for each player and games played when the
    # User no longer wants to continue playing

    print(f'''
Thanks for playing!\n
Results:\n
Games played: {games_played}\n
Player one: {player_one_wins} wins\n
Player two: {player_two_wins} wins
''')

# GAME LOGIC

os.system('clear')

# How to play

print('Welcome to Tic Tac Toe!\n')
print('Note that the board positions correspond to a PC numberpad:')
display_board(how_to_play_board_list)
print('Let\'s begin!\n')

# Playing

while game_on:

    while not winner_decided:
        
        player_turn_display()    # Standard round logic
        board_list = player_turn(board_list, current_player)
        display_board(board_list)
    
        check_for_winner(board_list)    # Checking for a winner
        check_for_stalemate(board_list)    # Checking for a stalemate

        # Changing which player's turn it is
        current_player = change_players_turn(current_player)
    
    game_on = play_again_check()    # Asking the user if they want to play again

# Displaying the results of all games played
display_game_results(games_played, player_one_wins, player_two_wins)
