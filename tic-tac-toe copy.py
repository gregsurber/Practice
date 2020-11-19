# Tic-Tac-Toe game in python, using Object Oriented Programming techniques
# Greg Surber
# CS 506 Fall 2020
# City University of Seattle


from os import system, name
# this will allow us to clear the screen, making the board easier to see


class Board():
    """ Establish the playing board for our game of tic-tac-toe"""

    def __init__(self):
        self.squares = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(" %s | %s | %s " %
              (self.squares[1], self.squares[2], self.squares[3]))
        print("-----------")
        print(" %s | %s | %s " %
              (self.squares[4], self.squares[5], self.squares[6]))
        print("-----------")
        print(" %s | %s | %s " %
              (self.squares[7], self.squares[8], self.squares[9]))

    # create class method to update the board
    def update_square(self, square_no, player):
        if self.squares[square_no] == " ":
            self.squares[square_no] = player

        else:
            print("That square is taken. Try a different one.")
            # clear_screen()

    # determine a winner
    def is_winner(self, player):
        # creat list of all possible winning combinations
        for combo in [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]:
            result = True
            # check if any winning cominations are held by player
            for square_no in combo:
                if self.squares[square_no] != player:
                    result = False

            if result == True:
                return True
        return False

    # Check for a tie game

    def is_tie(self):
        filled_squares = 0
        for square in self.squares:
            if square != " ":
                filled_squares += 1
        if filled_squares == 9:
            return True
        else:
            return False

    def reset_game(self):
        self.squares = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def ai_player(self, player):
        # have the AI player select the center square, if it is open
        if self.squares[5] == " ":
            self.update_square(5, player)
            file = open('tictactoe.txt', 'a')
            o_play = ["Computer played in square: 5 "]
            file.write(str(o_play) + '\n')
            file.close()
        else:
            # have the AI player select a random open square to play in
            for i in range(1, 10):
                if self.squares[i] == " ":
                    self.update_square(i, player)
                    file = open('tictactoe.txt', 'a')
                    o_play = ["Computer played in square: " + str(i)]
                    file.write(str(o_play) + '\n')
                    file.close()
                    break


board = Board()


def print_header():
    print("Let's play Tic-Tac-Toe!\n")


def clear_screen():
    # calling these three functions will clear any extra noise from the screen and re-draw the board, with
    # all moves still showing
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")
    print_header()
    board.display()


while True:
    clear_screen()
    # Get the play for player 'X'
    # using player 'X' choice, update the playing board
    try:
        # Check that the user entered an integer
        x_choice = int(input('\n Player X) Please make your move > '))

    except ValueError:
        # If the user put in a non-integer, tell them only integers allowed
<<<<<<< HEAD
        print("\nOnly numbers, please. Try again.")
        x_choice = int(input('\n Player X) Please make your move > '))
=======
        print("\nOnly numbers, please. Try again.")
        continue
>>>>>>> 255a8274ec7e88171c5ce479d3d1163f26022cfb
    else:
        # Verify that the user entered an integer in the usable range of 1 - 9
        if x_choice > 0 and x_choice < 10:
            # If the user did enter a valid integer, update the board with their move
<<<<<<< HEAD
            board.update_square(x_choice, "X")
        else:
            print("\n Only numbers between 1 and 9, please.")
    # clear the screen in preparation for player 'O' move
    # clear_screen()

=======
            board.update_square(x_choice, "X")
            file = open('tictactoe.txt', 'a')
            x_play = ["Player 'X' played in square: " + str(x_choice)]
            file.write(str(x_play) + '\n')
            file.close()
        else:
            print("\n Only numbers between 1 and 9, please.")
            continue

>>>>>>> 255a8274ec7e88171c5ce479d3d1163f26022cfb
    # check if user "X" has won
    if board.is_winner("X"):
        print("\n Player X has won!")
        file = open('tictactoe.txt', 'a')
        x_win = ["Player 'X' has won!"]
        file.write(str(x_win) + '\n\n\n')
        file.close()
        play_again = input(" Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset_game()
            continue
        else:
            with open('tictactoe.txt', 'r') as plays:
                print(plays.read())
            break

    # check if tie game
    if board.is_tie():
        print("\n It's a tie! \n")
        file = open('tictactoe.txt', 'a')
        tie_score = ["It's a tie!"]
        file.write(str(tie_score) + '\n\n\n')
        file.close()
        play_again = input(" Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset_game()
            continue
        else:
            with open('tictactoe.txt', 'r') as plays:
                print(plays.read())
            break

    clear_screen()

    # get player 'O' move
    # o_choice = int(input('\nO) Please make your move >'))

    # give the AI a move
    board.ai_player("O")

    # update playing board with player 'O' choise
    # board.update_square(o_choice, "O")
    clear_screen()
    # check if user "O" has won
    if board.is_winner("O"):
        print("\n Player O has won!")
        file = open('tictactoe.txt', 'a')
        o_win = ["Player 'O' has won!"]
        file.write(str(o_win) + '\n\n\n')
        file.close()
        play_again = input("\n Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset_game()
            continue
        else:
            with open('tictactoe.txt', 'r') as plays:
                print(plays.read())

            break


# check if tie game
    if board.is_tie():
        print("\n It's a tie! \n")
        play_again = input(" Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset_game()
            continue
        else:
            with open('tictactoe.txt', 'r') as plays:
                print(plays.read())
            break

<<<<<<< HEAD
    clear_screen()
=======
   # clear_screen()
>>>>>>> 255a8274ec7e88171c5ce479d3d1163f26022cfb
