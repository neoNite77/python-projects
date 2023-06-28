"""
    Date: June 26, 2023
    Updated: June 27, 2023
    Description: Play a of tic-tac-toe against a computer
"""

from player import Human, Computer, GeniusComputer
import game
import time

def main():
    print("Hello welcome to Tic Tac Toe!")
    print("-----------------------------")
    print("1.) Play against regular computer")
    print("2.) Play against genius computer")
    print("3.) Regular computer VS. genius computer")
    print("4.) Exit Program")
    while True:
        choice = int(input("Enter a menu option: "))
        if choice == 1:
            print("Starting game...")
            print("You are Player X")
            time.sleep(1)
            x_player = Human("X")
            o_player = Computer("O")
            t = game.TicTacToe()
            game.play(t, x_player, o_player, print_game=True)
        elif choice == 2:
            print("Starting game...")
            print("You are Player X")
            time.sleep(1)
            x_player = Human("X")
            o_player = GeniusComputer("O")
            t = game.TicTacToe()
            game.play(t, x_player, o_player, print_game=True)
        elif choice == 3:
            print("Starting game...")
            print(f"Regular Computer: X")
            print(f"Genius Computer: O")
            x_wins = 0
            o_wins = 0
            ties = 0
            for _ in range (10):
                x_player = Computer("X")
                o_player = GeniusComputer("O")
                t = game.TicTacToe()
                result = game.play(t, x_player, o_player, print_game=False)
                if result == "X":
                    x_wins += 1
                elif result == "O":
                    o_wins += 1
                else:
                    ties += 1

            print(f"After 10 iterations, here is the score distributions: \
                \nX Wins: {x_wins} | O Wins: {o_wins} | Ties: {ties}")

        elif choice == 4:
            print("Exiting Program now...")
            break
        else:
            print("Invalid Menu Option entered. Please try again.")    

if __name__ == "__main__":
    main()