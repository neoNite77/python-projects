'''
    Date: 10/23/2023
    Description: Write a function, add_it_up(), that takes a single integer as input
    and returns the sum of the integers from zero to the input parameter.
    The function should return 0 if a non-integer is passed in.
'''

def add_it_up(num_list) -> int:
    sum = 0
    for num in num_list:
        sum+= num
    return sum

print(add_it_up([1,2,3,4,5]))