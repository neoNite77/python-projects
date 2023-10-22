'''
    Date: 10/21/23
    Description: Write a Python program that takes a list of integers as input and returns a
    new list containing only the even numbers from the input list. Additionally, square each
    even number in the new list.
'''

'''
    postcondition: returns a list that contains even squared numbers
'''
def square_even_numbers(list1):

    # Create a list using list comprehension to store only even intergers
    even_numbers = [x for x in list1 if x % 2 == 0]

    # Square each even number and create a new list
    square_numbers = [x**2 for x in even_numbers]

    return square_numbers

list1 = [1, 2, 3, 4, 5, 6]
print(square_even_numbers(list1))