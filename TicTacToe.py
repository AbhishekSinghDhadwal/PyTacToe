# Code to implement clear function
from os import system, name
# define our clear function


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Code for the game
# DisplayBoard acts as a print function to display the board at any given time


def DisplayBoard(board):
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print(f"-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f"-----------")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
# DisplayBoard(['X','X','X','X','X','X','X','X','X']) # Test Case
# IsWon is used in order to determine whether the match is won or not


def IsWon(board):
    # Check diagonals
    if (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6]):
        if board[4] == 'X' or board[4] == 'O':
            return True
    # Check rows
    for i in range(3):
        if (board[i] == board[i + 3] == board[i + 6]) and (board[i] == 'X' or board[i] == 'O'):
            return True

        if (board[3 * i] == board[3 * i + 1] == board[3 * i + 2]) and (board[3 * i] == 'X' or board[3 * i] == 'O'):
            return True
    # Final outside loops
    return False
# IsBoardFull will determine whether board is full, and if it is and match is not won, then we will declare a tie


def IsBoardFull(board):
    ctr=0
    for i in range(9):
        if(board[i] == 'X') or (board[i] == 'O'):
            ctr += 1
    return ctr == 9
# print(IsBoardFull(['X','X','X','X','X','X','X','X','X'])) # Test Case
# Function InputCheck - to compare whether input is already there in the game or not
# And handles input range errors if they may occur


def InputCheck(x,o,iplist):
    if x in iplist or o in iplist:
        print('Input has already been used ! Enter inputs again.')
        xip = int(input(f"Enter the position of X"))
        oip = int(input(f"Enter the position of O"))
        return InputCheck(xip,oip,iplist)
    elif x > 9 or x < 1 or o > 9 or o < 1:
        print('Invalid input been used ! Enter inputs again.')
        xip = int(input(f"Enter the position of X"))
        oip = int(input(f"Enter the position of O"))
        return InputCheck(xip,oip,iplist)
    else:
        iplist.append(x)
        iplist.append(o)
        return x, o, iplist


def TicTac():
    print("Welcome to the Tic Tac Toe game !")
    ip = input("Enter player one's choice: (X/O)")
    if (ip[0] == 'X') or (ip[0] == 'x'):
        print("Player one goes first !")
    else:
        print("Player two shall go first !")
    print("In order to play, enter numbers from 1 to 9 which correspond to the board")
    print("The positions correspond to your numpad as follows")
    disp = range(1,10)
    DisplayBoard(disp)

    # Set of pieces within the board
    board = ['','','','','','','','','']
    # Checks whether input has been taken already or not
    iplist = []
    ctr = 0
    while not IsBoardFull(board) and not IsWon(board) and ctr < 4:
        clear()
        print("The board positions are :")
        DisplayBoard(board)
        xip = int(input(f"Enter the position of X"))
        oip = int(input(f"Enter the position of O"))
        (xip, oip, iplist) = InputCheck(xip,oip,iplist)
        board[xip-1] = 'X'
        board[oip-1] = 'O'
        ctr += 1

    # End of while loop
    if not IsWon(board):
        print("The game is tied!")
    else:
        print("Congratulations !")
    DisplayBoard(board)
    play = input("Would you like to play again ?Y/N")
    if play == 'Y':
        TicTacToe()
    else:
        print("Thank you for playing !")
        exit(0)


def TicTacToe():
    try:
        TicTac()
    except:
        print("An error has occured, restarting game again!")
        TicTacToe()
    finally:
        print("Program stopped")


TicTacToe()

