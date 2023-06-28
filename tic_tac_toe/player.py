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
            square = input(self.letter + "\'s turn. Input move (0-8): ")
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
    
class GeniusComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # randomly choose one
        else:
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)["position"]
        return square
    
    def minimax(self, state, player):
        max_player = self.letter # yourself!
        other_player = "O" if player == "X" else "X" # the other player... so whatever letter is NOT used

        # first, we want to check if the previous move is a winner
        # this is our base case
        if state.current_winner == other_player:
            # we should return position AND score because we need to keep track of the score for 
            # for minimax to work
            return {"position" : None,
                    "score": 1 * (state.num_empty_squares() + 1) if other_player == max_player else - 1 * (
                        state.num_empty_squares() + 1)
                        }
        elif not state.empty_squares(): # no empty squares
            return {"position": None, "score":0}
        
        if player == max_player:
            best = {"position": None, "score": -math.inf} # each score should maximize (be larger)
        else:
            best = {"position": None, "score": math.inf} # each score should minimize

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player) # now, we alternate players
            # step 3: undo the move
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score["position"] = possible_move # otherwise this will get messed up from the recursion
            # step 4: update the dicitionaires if necessary
            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score #replace best
            else: # but minimize the other player
                if sim_score["score"] < best["score"]:
                    best = sim_score # replace best

        return best



