from calculator import Calculator

def display_menu():
    print("Welcome to the Calculator App!")
    print("------------------------------")
    print("1.) Use Simple Calculator")
    print("2.) Exit")

def get_number_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    while True:
        display_menu()
        choice = int(get_number_input("Enter a menu option: "))
        if choice == 1:
            calculator = Calculator()
            calculator.menu()
            calculator.choice()
        elif choice == 2:
            print("Exiting program...")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()