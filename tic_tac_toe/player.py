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
        pass

class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass