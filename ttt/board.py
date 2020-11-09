from os import system, name
# this will allow us to clear the screen, making the board easier to see

class Board():
    """ Establish the playing board for our game of tic-tac-toe"""
    def __init__(self):
        self.squares = [" "," "," "," "," "," "," "," "," "," "]
    def print_header():
        print("Let's play Tic-Tac-Toe!\n")

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
        # creat list of all possible winning combinations
        for combo in [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
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
