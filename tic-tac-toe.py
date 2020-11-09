# Tic-Tac-Toe game in python, using Object Oriented Programming techniques
# Greg Surber
# CS 506 Fall 2020
# City University of Seattle


import os
# this will allow us to clear the screen, making the board easier to see
os.system("cls") 

class Board():
    """ Establish the playing board for our game of tic-tac-toe"""
    def __init__(self):
        self.squares = [" "," "," "," "," "," "," "," "," "," "]

    def display(self):
        print(" %s | %s | %s " %(self.squares[1],self.squares[2], self.squares[3]))
        print("-----------")
        print(" %s | %s | %s " %(self.squares[4],self.squares[5], self.squares[6]))
        print("-----------")
        print(" %s | %s | %s " %(self.squares[7],self.squares[8], self.squares[9]))
    
    # create class method to update the board
    def update_square(self, square_no, player):
        if  self.squares[square_no] == " ":
            self.squares[square_no] = player
        else:
            print("That square is taken. Try a different one.")
            #clear_screen()            

    # determine a winner
    def is_winner(self, player):
        # if one player occupies squares 1 -3 (the entire top row), then they have won
        if self.squares[1]  == player and self.squares[2] == player and self.squares[3] == player:
            return True
        # if one player occupies squares 3 - 5 (the entire middle row), then they have won
        elif self.squares[3]  == player and self.squares[4] == player and self.squares[5] == player:
            return True
        # if one player occupies squares 7 - 9 (the entire bottom row), then they have won
        elif self.squares[7]  == player and self.squares[8] == player and self.squares[9] == player:
            return True
        # if one player occupies squares 1, 4, and 7 (the left column), then they have won
        elif self.squares[1]  == player and self.squares[4] == player and self.squares[7] == player:
            return True
        # if one player occupies squares 2, 5, and 8 (the entire middle column), then they have won
        elif self.squares[2]  == player and self.squares[5] == player and self.squares[8] == player:
            return True
        # if one player occupied squares 3, 6, and 9 (the entire right column), then they have won    
        elif self.squares[3]  == player and self.squares[6] == player and self.squares[9] == player:
            return True
        # if one player occupies squares 3, 5, and 7 (a diagonal), then they have won
        elif self.squares[3]  == player and self.squares[5] == player and self.squares[7] == player:
            return True
        # if one player occupies squares 1, 5, and 9 (the other diagonal), then they have won
        elif self.squares[1]  == player and self.squares[5] == player and self.squares[9] == player:
            return True
        else:
            # if no player occupies a complete winning move, then continue play
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
        self.squares = [" "," "," "," "," "," "," "," "," "," "]

    def ai_player(self, player):
        # have the AI player select the center square, if it is open
        if self.squares[5] == " ":
            self.update_square(5, player)
        else:
        # have the AI player select a random open square to play in
            for i in range(1,10):
                if self.squares[i] == " ":
                    self.update_square(i, player)
                    break

board = Board()

def print_header():
    print("Let's play Tic-Tac-Toe!\n")

def clear_screen():
    # calling these three functions will clear any extra noise from the screen and re-draw the board, with 
    # all moves still showing
    os.system("cls")
    print_header()
    board.display()

while True:
    clear_screen()
    # Get the play for player 'X'
    x_choice = int(input('\n Player X) Please make your move > '))
    # using player 'X' choice, update the playing board
    board.update_square(x_choice, "X")

    # clear the screen in preparation for player 'O' move
    clear_screen()

    # check if user "X" has won
    if board.is_winner("X"):
        print("\n Player X has won!")
        play_again = input(" Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset_game()
            continue
        else:
            break

    # check if tie game
    if board.is_tie():
        print("\n It's a tie! \n")
        play_again = input(" Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset_game()
            continue
        else:
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
        play_again = input("\n Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset_game()
            continue
        else:
            break



    # check if tie game
    if board.is_tie():
        print("\n It's a tie! \n")
        play_again = input(" Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset_game()
            continue
        else:
            break

    clear_screen()