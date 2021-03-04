import random


def display_board(board):
    print(board[0])
    print(board[1])
    print(board[2])


def check_win(board, player):
    return ((board[0][0].upper() == player and board[0][1].upper() == player and board[0][2].upper() == player) or
            (board[1][0].upper() == player and board[1][1].upper() == player and board[1][2].upper() == player) or
            (board[2][0].upper() == player and board[2][1].upper() == player and board[2][2].upper() == player) or
            (board[0][0].upper() == player and board[1][0].upper() == player and board[2][0].upper() == player) or
            (board[0][1].upper() == player and board[1][1].upper() == player and board[2][1].upper() == player) or
            (board[0][2].upper() == player and board[1][2].upper() == player and board[2][2].upper() == player) or
            (board[0][0].upper() == player and board[1][1].upper() == player and board[2][2].upper() == player) or
            (board[0][2].upper() == player and board[1][1].upper() == player and board[2][0].upper() == player))


def x_o():
    marker = ""
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player1 please choose your marker (x or o): ").upper()
    if marker == "O":
        return 'O', 'X'
    else:
        return 'X', 'O'


def player_choice(board):
    while True:
        row = input("enter the row you choose: (0-2) ")
        if row not in ['0', '1', '2']:
            print("This row isn't available, please choose another")
            continue
        column = input("enter the column you choose: (0-2)")
        if column not in ['0', '1', '2']:
            print("This column isn't available, please try again")
            continue
        if space_check(board, int(row), int(column)):
            return int(row), int(column)
            break
        else:
            print("this space isn't available please choose another")
            continue


def place_choice(board, row, column, player):
    board[row][column] = player


def space_check(board, row, column):
    return board[row][column] == "_"


def replay():
    return input("Do you wish to play again? (y/n)").upper() == "Y"


def choose_first():
    num = random.randint(0, 1)
    if num == 0:
        return "player 2"
    else:
        return "player 1"


def full_board_check(board):

    for i in range(3):
        for p in range(3):
            if space_check(board, i, p):
                return False
    return True


def next_turn_win():
    # add the situations where a player can win in 1 move, while the space needed isn't already occupied
    # and print that the player will either lose or win depending on the situation.
    pass


while True:
    ttt_board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]
    player1_mark, player2_mark = x_o()
    turn = choose_first()
    print(f"{turn} will go first.")
    play = input("Do you want to start the game? (y/n): ").upper()
    if play == "Y":
        game_on = True
        display_board(ttt_board)
    else:
        game_on = False

    while game_on:
        if turn == "player 1":
            print("player 1's turn:")
            x, y = player_choice(ttt_board)
            place_choice(ttt_board, x, y, player1_mark)
            display_board(ttt_board)
            if check_win(ttt_board, player1_mark):
                display_board(ttt_board)
                print(f"congratulations player one ({player1_mark}) is the winner")
                game_on = False
            elif full_board_check(ttt_board):
                display_board(ttt_board)
                print("It's a draw!")
                break
            else:
                turn = "player 2"

        else:
            print("player 2's turn:")
            x, y = player_choice(ttt_board)
            place_choice(ttt_board, x, y, player2_mark)
            display_board(ttt_board)
            if check_win(ttt_board, player2_mark):
                display_board(ttt_board)
                print(f"congratulations player two ({player2_mark}) is the winner")
                game_on = False
            elif full_board_check(ttt_board):
                display_board(ttt_board)
                print("It's a draw!")
                break
            else:
                turn = "player 1"

    if not replay():
        break


