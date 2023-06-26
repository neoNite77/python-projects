"""
    Date: June 22, 2023
    Updated: June 26, 2023
    Description: Play a game of hangman and be able to guess the word that the computer has chosen!
"""
import random
import string
from player import Player
from words import wordList

"""
    Computer will retrieve a random word from the list

    precondition: len(words) > 0
    postcondition: returns a printed statement of the random number
"""
def get_valid_word(wordList):
    word = random.choice(wordList)
    
    # Keep iterating through the list until it reaches a word that doesn't have a space or dash in it.
    while '-' in word or ' ' in word:
        word = random.choice(wordList)
    return word.upper()


"""
    User will guess random number until they guess correctly

    precondition: len(words) > 0
    postcondition: returns a printed statement of the random number
"""
def hangman(p1):
    word = get_valid_word(wordList)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0 and p1.lives > 0:
        # letters used
        # " ".join(['a', 'b', 'cd']) --> "a b cd"
        print(f"You have {p1.lives} lives lefts and you have used these letters: "," ".join(used_letters))

        # What current word is (ie. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))
        
        # getting user input
        guessed_letter = input("Guess a letter: ").upper()
        # Checks if the user only entered one letter
        if len(guessed_letter) > 1:
            print("Please enter one character only. Please try again: ")
            continue 
        if guessed_letter in alphabet - used_letters:
            used_letters.add(guessed_letter)
            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)
            else:
                #take away a life if wrong
                p1.lives = p1.lives - 1
                print("Letter is not in word.")
        elif guessed_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print("Invalid character. Please try again.")
    # Gets to here when len(word_letters) == 0 OR when lives == 0 
    if p1.lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the word", word, "!!")

def main():
    p1 = Player()
    hangman(p1)

if __name__ == "__main__":
    main()