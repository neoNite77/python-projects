'''
    Date: 10/21/2023
    Description: Write a Python function that takes a list of integers as input and returns
     a new list containing only the prime numbers from the input list. Additionally,
     sum all the prime numbers in the new list.
'''
import math

# Check and validate whether a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    # Iterate through odd integers from 3 to the square root of the number
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

# Sum all prime numbers in a list
def find_and_sum_primes(input_list):
    primes_list = []

    for i in input_list:
        if is_prime(i):
            primes_list.append(i)
    sum = 0
    for x in primes_list:
        sum += x
    return [[primes_list], sum]


# Test the function
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = find_and_sum_primes(input_list)
print("Prime numbers:", result[0])  # Expected output: [2, 3, 5, 7]
print("Sum of prime numbers:", result[1])  # Expected output: 17