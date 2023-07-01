from operations import Operations

class Calculator():

    @staticmethod
    def menu():
        print("Select an operation.")
        print("--------------------")
        print("1.) Add")
        print("2.) Subtract")
        print("3.) Multiply")
        print("4.) Divide")
        print("5.) Square")
        print("6.) Modulus")
        print("7.) Square root")
        print("8.) Exit Simple Calculator")

    @staticmethod
    def choice():
        eval = Operations()
        while True:
            choice = int(input("Select an operation to calculate:"))
            if choice == 1:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                result = eval.add(num1, num2)
                print(f"Result: {result}")