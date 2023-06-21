"""
    Date: June 20, 2023
    Description: User will have to beat the computer at its own game. If they guess the random
                 number correctly, then they win the game!
"""
import random

"""
    User will guess random number until they guess correctly

    precondition: number > 1
    postcondition: returns a printed statement of the random number
"""
def guess(number):
    random_number = random.randint(1, number)
    guess = 0

    # Loop until the user guesses the correct number
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {random_number}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    return f"Yay! You guessed the right number! {random_number} is correct!"

"""
    Computer guesses random number until it guesses correctly

    precondition: number > 1
    postcondition: returns a printed statement of the random number
"""

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    # Computer will keep guessing until 
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            # could be either low or high
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    return f"The computer has guessed your number correctly! {guess} is your number!"

def main():
    print("Hello, welcome to number guesser!")
    print("---------------------------------")
    print("1.) Guess computer's number")
    print("2.) Computer guesses player's number")
    print("3.) Exit program")
    while True:
        choice = int(input("Enter a menu option: "))
        if choice == 1:
            number = 0
            while number < 1:
                number = int(input("Hello! Please enter a number greater than 1:"))
            print(guess(number))
        elif choice == 2:
            number = 0
            while number < 1:
                number = int(input("Hello! Please enter a number greater than 1:"))
            print(computer_guess(number))
        elif choice == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid menu option entered. Try again!")

if __name__ == "__main__":
    main()