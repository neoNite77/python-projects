"""
    Date: June 20, 2023
    Description: Program will run as a madlibs game where users can enter input
"""

import random

"""
    Start the regular mad labs game.
"""


def madLibs():
    print("\nWelcome to Mad Libs!")
    print("--------------------")

    # User input to fill in the mad lib statements
    name = input("Enter a name: ")
    adj = input("Enter an adjective: ")

    # Store input into a formatted string
    statement1 = f"My name is {name}. I am very {adj}!"

    print(statement1)


def main():
    madLibs()


if __name__ == "__main__":
    print("Welcome!")
    print("1.) Mad Libs")
    print("2.) Random Mad Libs")
    print("3.) Exit Program")
    while True:
        choice = input("Hi! Enter an option (0 - 2): ")
        if choice == "1":
            main()
        elif choice == "2":
            pass
        elif choice == "3":
            break
        else:
            print("Invalid Option. Please enter again!")
