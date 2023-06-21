"""
    Date: June 20, 2023
    Description: Program will run as a madlibs game where users can enter input
"""

print("Welcome to Mad Libs!")
print("--------------------")

# User input to fill in the mad lib statements
name = input("Enter a name: ")
adj = input("Enter an adjective: ")

# Store input into a formatted string
statement1 = f"My name is {name}. I am very {adj}!"

print(statement1)
