"""
    Date: June 26, 2023
    Description: Play a of tic-tac-toe against a computer
"""

from player import Human, Computer
import game

def main():
    x_player = Human("X")
    o_player = Computer("O")
    t = game.TicTacToe()
    game.play(t, x_player, o_player, print_game=True)

if __name__ == "__main__":
    main()