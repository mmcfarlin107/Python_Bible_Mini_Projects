# This is a game of tic-tac-toe

# using list comprehension below to create tic-tac-toe board

board = ["_" for i in range(0, 9)]

# global variable being used to watch for a tie
counter = 0


# prints board with updated content every time a player makes a move
def print_board():
    print()
    print(
        f" {board[0]} | {board[1]} | {board[2]} \n {board[3]} | {board[4]} | "
        f"{board[5]} \n {board[6]} | {board[7]} | {board[8]} "
    )
    print()


# Takes players move choice as an input
# If the input is a valid number for the game and the space is not taken, the player gets the spot.
# If the spot is taken or the input is not a valid number, the function uses recursion to call itself again.
def player_move(letter):
    move = int(input("What space would you like player " + letter + " (1-9)?: ").strip())
    if move in range(1, 10) and board[move - 1] == "_":
        board[move - 1] = letter
        global counter
        counter += 1
    else:
        print('Invalid Choice! Choose again...')
        player_move(letter)


def check_winner(letter):
    # checking horizontal
    if board[0] == letter and board[1] == letter and board[2] == letter:
        return True
    elif board[3] == letter and board[4] == letter and board[5] == letter:
        return True
    elif board[6] == letter and board[7] == letter and board[8] == letter:
        return True
    # checking diagonal
    elif board[0] == letter and board[3] == letter and board[6] == letter:
        return True
    elif board[1] == letter and board[4] == letter and board[7] == letter:
        return True
    elif board[2] == letter and board[5] == letter and board[8] == letter:
        return True
    elif board[0] == letter and board[4] == letter and board[8] == letter:
        return True
    elif board[2] == letter and board[4] == letter and board[6] == letter:
        return True
    else:
        return False


# endless loop for game to never officially end unless 'break' from a win

while True:
    print_board()
    player_move('X')
    print_board()
    if check_winner('X'):
        print('Player X Wins!')
        break

    # if counter is 9 that means that all the spaces are full and still nobody has won. It is incremented during the
    # player_move function if valid move choosen.

    if counter == 9:
        print("It's a Draw!")
        break
    player_move('O')
    print_board()
    if check_winner('O'):
        print('Player O Wins!')
        break
    # if counter is 9 that means that all the spaces are full and still nobody has won. It is incremented during the
    # player_move function if valid move choosen.

    if counter == 9:
        print("It's a Draw!")
        break
