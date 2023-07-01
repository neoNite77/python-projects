import math

class Operations():
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError("Error: Can not divide by zero")
        
    def square(self, a):
        return a**2
    
    def modulus(self, a, b):
        return a % b
    
    def square_root(self, a):
        if a < 0:
           raise ValueError("Error: Cannot calculate square root of a negative number.")
        return math.sqrt(a)