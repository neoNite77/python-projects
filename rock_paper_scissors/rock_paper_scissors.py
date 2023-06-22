"""
    Date: June 21, 2023
    Description: User and computer will go against each other in a game of rock paper sissors!
"""
import random

"""
    Initiate game of rock paper scissors

    postcondition: returns a string value determining the outcome of the game
"""
def play():
    user = input("What is your choice?\n'r' for rock, 'p' for paper, 's' for scissors: \n").lower()
    while user != 'r' and user != 'p' and user != 's':
        user = input("Invalid choice!!! \nChoose 'r' for rock, 'p' for paper, 's' for scissors: \n").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print(display_match_up(user, computer))
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
        print(display_match_up(player, opponent))
        return True
    print(display_match_up(player, opponent))
    
"""
    Return a string containing both the player and the opponents choice

    postcondition: return a string value
"""
def display_match_up(player, opponent):
    return f'Player Chose: {player} | OpponentsChose: {opponent}'
    
def number_of_rounds():
    number = int(input("Enter the number of rounds you would like to play: "))
    return number

def display_menu_option():
    print("Welcome to Rock Paper Scissors")
    print("------------------------------")
    print("1.) Play game")
    print("2.) Exit")
    
def main():
    display_menu_option()
    while True:
        choice = int(input("Enter a menu option: "))
        if choice == 1:
            iterations = number_of_rounds()
            for i in range (iterations):
                print(play())
            print("Thanks for playing! \n")
            display_menu_option()

        elif choice == 2:
            print("Exiting program...")
            break
        else:
            print("Invalid menu option entered. Try again!")

if __name__ == '__main__':
    main()