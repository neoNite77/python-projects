"""
    Date: June 20, 2023
    Description: Program will run as a madlibs game where users can enter input
"""
import random
import madlibsTemplates

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

    print(statement1 + "\n")

def randomMadLibs():
    print("\nYou are playing random Mad Labs!")
    print("--------------------------------")
    number = random.randrange(0,3)
    string = madlibsTemplates.templates[number]

    name = input("Enter a name: ")
    print(string.format(name) + "\n")

def main():
    print("Welcome!")
    print("1.) Mad Libs")
    print("2.) Random Mad Libs")
    print("3.) Exit Program")
    while True:
        choice = input("Hello! Enter an option (1 - 3): ")
        if choice == "1":
            madLibs()
        elif choice == "2":
            randomMadLibs()
        elif choice == "3":
            print("Exiting program now...")
            break
        else:
            print("Invalid Option. Please enter again!")


if __name__ == "__main__":
    main()