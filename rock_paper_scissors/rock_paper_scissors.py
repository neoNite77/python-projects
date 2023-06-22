"""
    Date: June 21, 2023
    Description: User and computer will go against each other in a game of rock paper sissors!
"""
import random

"""
    Initiate game of rock paper scissors
"""
def play():
    user = input("What is your choice?\n'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie!'
    
    if is_win(user, computer):
        return 'You Won!'
    
    return 'You lost!'

"""
    Determine whether the player or the computer wins the game
    Rock > Scissors | Scissors < Paper | Paper > Rock

    postcondition: returns a true if player wins against the computer
"""
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    
def main():
    print(play())

if __name__ == '__main__':
    main()