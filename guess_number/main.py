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

def main():
    number = 0
    while number < 1:
        number = int(input("Hello! Please enter a number greater than 1:"))
    print(guess(number))

if __name__ == "__main__":
    main()