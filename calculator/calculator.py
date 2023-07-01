from operations import Operations
import time
import sys

class Calculator():

    def menu(self):
        operation_string = ["add", "subtract", "multiply", 
                            "divide", "square", "modulus", 
                            "square root"]
        eval = Operations()
        result = None # Initialize result with none
        while True:
            print("\nSelect an operation.")
            print("--------------------")
            print("1.) Add")
            print("2.) Subtract")
            print("3.) Multiply")
            print("4.) Divide")
            print("5.) Square")
            print("6.) Modulus")
            print("7.) Square root")
            print("8.) Exit Simple Calculator")

            choice = int(self.get_number_input("Select an operation to calculate a result: "))
            if choice in [1, 2, 3, 4]:
                print(f"\nYou selected the {operation_string[choice-1]} operation: ")
                # num1 and num2 is assigned the tulple that is returned from the function
                num1, num2 = self.get_two_numbers()
                if choice == 1:
                    result = eval.add(num1, num2)
                elif choice == 2:
                    result = eval.subtract(num1, num2)
                elif choice == 3:
                    result = eval.multiply(num1, num2)
                elif choice == 4:
                    try: 
                        result = eval.divide(num1, num2)
                    except ZeroDivisionError as e:
                        print(e)
            elif choice in [5, 6, 7]:
                print(f"\nYou selected the {operation_string[choice-1]} operation: ")
                num1 = int(self.get_number_input("Enter a number: "))
                if choice == 5: 
                    result = eval.square(num1)
                if choice == 6:
                    result = eval.modulus(num1)
                if choice == 7:
                    try:
                        result = eval.square_root(num1)
                    except ValueError as e:
                        result = str(e)
            elif choice == 8:
                print("Exiting Simple Calculator...")
                break
            else:
                print("Invalid input. Please try again")
                continue # Skip rest of the loop and restart menu
            print(f"Result: {result}")
            # Delay process by one second
            time.sleep(0.8)

    def get_number_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter an integer.")
            except KeyboardInterrupt:
                print("\nProgram interrupted by user. Exiting Calculator...")
                sys.exit(0)  # Exit the program
    
    def get_two_numbers(self):
        num1 = int(self.get_number_input("Enter the first number: "))
        num2 = int(self.get_number_input("Enter the second number: "))
        # Python returns a single object containing a tuple of the two numbers
        return num1, num2