import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
    
    # We want all players to get their next move given in a game
    def get_move(self, game):
        pass

class Computer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\'s turn. Input move(0-8): ")
            """
                We're going to check that this is a correct value by trying to cast
                it to an integer, and if it's not, then we say it's invalid
                if that spot is not available on the board, we also say it is invalid
            """
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if thse are successful, then good!
            except ValueError:
                print("Invalid square. Try again")
        return val


